import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from core.tool_router import execute_tool_command
from core.memory import Memory
from core.task_graph import TaskGraph
from core.architect import ArchitectAgent
from core.fixer import FixerAgent
from core.test_runner import TestRunner


# =========================
# SYSTEM INIT
# =========================
memory = Memory()
task_graph = TaskGraph()
architect = ArchitectAgent()

test_runner = TestRunner(workspace="workspace")


# =========================
# MODEL CLIENT
# =========================
model_client = OpenAIChatCompletionClient(
    model="qwen2.5-coder:32b",
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


# =========================
# AGENTS
# =========================
planner = AssistantAgent(
    name="Planner",
    model_client=model_client,
    system_message="You break problems into structured step-by-step plans."
)

coder = AssistantAgent(
    name="Coder",
    model_client=model_client,
    system_message="""
You are a senior software engineer.

You ONLY output TOOL commands.

Allowed tools:
TOOL: write_file("path", "content")
TOOL: run_python("file")
TOOL: run_shell("cmd")

Rules:
- You can create MULTIPLE files
- Always use correct file paths
- No explanations
- No markdown
"""
)

critic = AssistantAgent(
    name="Critic",
    model_client=model_client,
    system_message="You review code quality, bugs, structure, and improvements."
)

fixer = FixerAgent(model_client)


# =========================
# TOOL EXECUTION
# =========================
def run_tool_execution(output: str):
    results = []

    for line in output.split("\n"):
        line = line.strip()

        if line.startswith("TOOL:"):
            command = line.replace("TOOL:", "").strip()

            print(f"\n⚙️ EXECUTING: {command}")

            result = execute_tool_command(command)

            print("RESULT:", result)

            results.append(result)

    return results


# =========================
# MAIN v0.7 LOOP
# =========================
async def main():

    user_request = """
Build a simple calculator project.

Requirements:
- add, subtract, multiply, divide
- clean Python structure
- separate functions
- include test file
"""

    print("\n🏗 Generating Architecture...")
    architecture = architect.generate_architecture(user_request)
    memory.add("architecture", architecture)
    print(architecture)

    # =========================
    # TASK GRAPH (v0.7)
    # =========================
    task_graph.add_task("Planning")
    task_graph.add_task("Code Generation", ["Planning"])
    task_graph.add_task("Testing", ["Code Generation"])
    task_graph.add_task("Review", ["Testing"])

    max_attempts = 5

    while True:

        task = task_graph.next_task()

        if not task:
            break

        print(f"\n📌 TASK: {task['task']}")

        # =========================
        # PLANNING
        # =========================
        if task["task"] == "Planning":

            plan = await planner.run(
                task=f"""
User Request:
{user_request}

Architecture:
{architecture}
"""
            )

            plan_output = plan.messages[-1].content
            memory.add("plan", plan_output)

            print("\n📌 PLAN:\n", plan_output)


        # =========================
        # CODE GENERATION + SELF FIX LOOP
        # =========================
        elif task["task"] == "Code Generation":

            attempt = 0
            success = False
            code = None
            tool_results = None

            while not success and attempt < max_attempts:

                attempt += 1
                print(f"\n🔁 ATTEMPT {attempt}")

                # FIRST GENERATION
                if code is None:

                    result = await coder.run(
                        task=f"""
Architecture:
{architecture}

Plan:
{memory.get('plan')}
"""
                    )

                    code = result.messages[-1].content

                # FIX LOOP
                else:

                    test_results = test_runner.run_tests()

                    code = await fixer.fix(
                        code=code,
                        errors=str(tool_results),
                        review=str(memory.get("review", "")),
                        test_results=str(test_results)
                    )

                memory.add("generated_code", code)
                print("\n💻 CODE:\n", code)

                # EXECUTE TOOLS
                tool_results = run_tool_execution(code)
                memory.add("tool_results", str(tool_results))

                # RUN TESTS
                test_results = test_runner.run_tests()

                print("\n🧪 TEST RESULTS:")
                for t in test_results:
                    print(t)

                # SUCCESS CHECK
                if all(t["success"] for t in test_results) and not any(
                    "error" in str(x).lower() for x in tool_results
                ):
                    success = True
                    print("\n✅ CODE SUCCESSFUL")
                else:
                    print("\n⚠️ FAIL → FIXING...")

        # =========================
        # TEST + REVIEW
        # =========================
        elif task["task"] == "Testing":

            test_results = test_runner.run_tests()
            memory.add("test_results", str(test_results))

            print("\n🧪 FINAL TEST RESULTS:")
            for t in test_results:
                print(t)

        elif task["task"] == "Review":

            review = await critic.run(
                task=f"""
Code:
{memory.get('generated_code')}

Test Results:
{memory.get('test_results')}

Tool Results:
{memory.get('tool_results')}
"""
            )

            review_output = review.messages[-1].content
            memory.add("review", review_output)

            print("\n🧠 REVIEW:\n", review_output)

        task_graph.complete(task["task"])

    print("\n🚀 Mindloom v0.7 COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    asyncio.run(main())