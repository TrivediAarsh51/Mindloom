import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from core.tool_router import execute_tool_command


# =========================
# MODEL (OLLAMA)
# =========================
model_client = OpenAIChatCompletionClient(
    model="qwen2.5-coder:14b",
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
    system_message="""
You are a senior software architect.
Create structured step-by-step implementation plans.
"""
)

coder = AssistantAgent(
    name="Coder",
    model_client=model_client,
    system_message="""
You are a coding agent.

You MUST output ONLY TOOL commands.

STRICT FORMAT:

TOOL: write_file("filepath", "content")
TOOL: run_python("filepath")
TOOL: run_shell("command")

Examples:

TOOL: write_file("workspace/hello.py", "print('Hello World')")
TOOL: run_python("workspace/hello.py")

Rules:
- Use double quotes around ALL arguments
- No markdown
- No explanations
- No extra text
- Output ONLY TOOL commands
"""
)

critic = AssistantAgent(
    name="Critic",
    model_client=model_client,
    system_message="""
You are a strict code reviewer.
Find bugs, mistakes, and improvements.
"""
)


# =========================
# TOOL EXECUTION
# =========================
def run_tool_execution(agent_output: str):
    lines = agent_output.split("\n")
    results = []

    for line in lines:
        line = line.strip()

        if line.startswith("TOOL:"):
            command = line.replace("TOOL:", "").strip()

            print(f"\n⚙️ Executing: {command}")

            result = execute_tool_command(command)

            print("Result:", result)

            results.append(result)

    return results


# =========================
# MAIN AUTONOMOUS LOOP
# =========================
async def main():

    max_iterations = 3
    task = "Create a Python file that prints Hello World"

    for i in range(max_iterations):

        print(f"\n🚀 ITERATION {i+1}")

        # 1. PLANNER
        plan = await planner.run(task=task)
        plan_output = plan.messages[-1].content

        print("\n📌 PLAN:\n", plan_output)

        # 2. CODER
        code = await coder.run(task=plan_output)
        coder_output = code.messages[-1].content

        print("\n🤖 CODER OUTPUT:\n", coder_output)

        # 3. EXECUTE TOOLS
        tool_results = run_tool_execution(coder_output)

        print("\n⚙️ TOOL RESULTS:\n", tool_results)

        # 4. CRITIC REVIEW
        review = await critic.run(task=coder_output)
        critic_output = review.messages[-1].content

        print("\n🧠 CRITIC:\n", critic_output)

        # 5. FAILURE CHECK
        if any("error" in str(r).lower() for r in tool_results):
            task = f"""
Fix these issues and regenerate correct code:

Tool errors:
{tool_results}

Critic feedback:
{critic_output}
"""
        else:
            print("\n✅ SUCCESS - TASK COMPLETED")
            break


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    asyncio.run(main())