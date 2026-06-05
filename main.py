import asyncio
import json
import re
from pathlib import Path

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from core.tool_router import execute_tool_command
from core.memory import Memory
from core.task_graph import TaskGraph
from core.architect import ArchitectAgent
from core.fixer import FixerAgent
from core.test_runner import TestRunner


# =========================
# INIT
# =========================

workspace_dir = Path("workspace")
workspace_dir.mkdir(exist_ok=True)

memory = Memory()
task_graph = TaskGraph()
architect = ArchitectAgent()
test_runner = TestRunner(workspace=str(workspace_dir))

model_client = OpenAIChatCompletionClient(
    model="qwen2.5-coder:7b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model_info={
        "vision": False,
        "function_calling": False,
        "json_output": False,
        "structured_output": False,
        "family": "unknown",
    }
)

fixer = FixerAgent(model_client)


# =========================
# AGENTS
# =========================

planner = AssistantAgent(
    name="Planner",
    model_client=model_client,

    system_message="""
    You are a strict JSON generator.

    OUTPUT ONLY VALID JSON.

    NO TEXT BEFORE OR AFTER.

    NO LABELS LIKE "Planning", "Code Generation".

    FORMAT ONLY:

    {
    "backend": ["file.py"],
    "core": ["file.py"],
    "tests": ["file.py"]
    }
    """
)

coders = {
    "backend": AssistantAgent(
        name="Coder_backend",
        model_client=model_client,
        system_message="Only output TOOL commands."
    ),
    "core": AssistantAgent(
        name="Coder_core",
        model_client=model_client,
        system_message="Only output TOOL commands."
    ),
    "tests": AssistantAgent(
        name="Coder_tests",
        model_client=model_client,
        system_message="Only output TOOL commands."
    )
}

critic = AssistantAgent(
    name="Critic",
    model_client=model_client,
    system_message="Review code and return issues clearly."
)


# =========================
# SAFE HELPERS
# =========================

def extract_json(text: str):
    """Extract first JSON block safely"""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except:
        return None


def normalize_task(task_str: str):
    """ONLY accept module:file.py format"""
    if not isinstance(task_str, str):
        return None

    if ":" not in task_str:
        return None

    parts = task_str.split(":")

    if len(parts) != 2:
        return None

    module, file_name = parts

    if not file_name.endswith(".py"):
        return None

    return module, file_name


def run_tool_execution(agent_output: str):
    results = []

    for line in agent_output.split("\n"):
        line = line.strip()

        if line.startswith("TOOL:"):
            cmd = line.replace("TOOL:", "").strip()
            result = execute_tool_command(cmd)
            results.append(result)

    return results


# =========================
# TASK EXECUTION
# =========================

async def run_task(module, file_name):

    coder = coders.get(module)

    if not coder:
        print(f"⚠️ No coder for {module}")
        return

    code = None
    tool_results = None

    for attempt in range(5):

        if code is None:
            resp = await coder.run(task=f"Generate code for {file_name}")
            code = resp.messages[-1].content
        else:
            code = await fixer.fix(
                code=code,
                errors=str(tool_results),
                review=str(memory.get("review", "")),
                test_results=str(test_runner.run_tests())
            )

        tool_results = run_tool_execution(code)

        test_results = test_runner.run_tests()

        if all(r["success"] for r in test_results):
            break

    review = await critic.run(
        task=f"Review {file_name}\n\n{code}"
    )

    memory.add(f"{module}:{file_name}", review.messages[-1].content)


# =========================
# MAIN
# =========================

async def main():

    task_graph.save([])

    user_request = "Create a Python project with backend, core logic, and tests."

    architecture = architect.generate_architecture(user_request)
    memory.add("architecture", architecture)

    plan_resp = await planner.run(task=user_request)

    plan_output = plan_resp.messages[-1].content

    match = re.search(r"\{.*\}", plan_output, re.DOTALL)

    if not match:
        print("❌ Planner failed: no JSON found")
        print(plan_output)
        exit()

    try:
        module_plan = json.loads(match.group())
    except:
        print("❌ Planner returned invalid JSON")
        print(plan_output)
        exit()

    # =========================
    # TASK CREATION (STRICT)
    # =========================

    for module, files in module_plan.items():

        if not isinstance(files, list):
            continue

        for file in files:

            # MUST be string
            if not isinstance(file, str):
                continue

            # MUST be python file
            if not file.endswith(".py"):
                continue

            task = f"{module}:{file}"

            # FINAL VALIDATION (critical)
            if len(task.split(":")) != 2:
                continue

        task_graph.add_task(task)

        print(f"✅ Valid task added: {task}")

    # =========================
    # LOAD TASKS
    # =========================

    ready_tasks = [
        t for t in task_graph.load()
        if t["status"] == "pending"
    ]

    tasks = []

    for task in ready_tasks:

        normalized = normalize_task(task["task"])

        if not normalized:
            print(f"⚠️ Skipping corrupt task: {task['task']}")
            continue

        module, file_name = normalized

        tasks.append(run_task(module, file_name))


    await asyncio.gather(*tasks)

    print("\n✅ Mindloom v0.8 STABLE EXECUTION COMPLETE")


# =========================
# ENTRY
# =========================

if __name__ == "__main__":
    asyncio.run(main())