import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Connect Ollama
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

# Planner Agent
planner = AssistantAgent(
    name="Planner",
    model_client=model_client,
    system_message="""
    You are a senior software architect.
    Create structured implementation plans.
    """
)

# Coder Agent
coder = AssistantAgent(
    name="Coder",
    model_client=model_client,
    system_message="""
    You are an expert Python programmer.
    Write clean and efficient code.
    """
)

# Critic Agent
critic = AssistantAgent(
    name="Critic",
    model_client=model_client,
    system_message="""
    You review software and identify bugs,
    optimizations, and improvements.
    """
)

async def main():

    task = """
    Build a simple Python calculator app
    supporting:
    - addition
    - subtraction
    - multiplication
    - division
    """

    # STEP 1 — Planning
    print("\n===== PLANNER =====\n")

    plan = await planner.run(task=task)

    planner_output = plan.messages[-1].content

    print(planner_output)

    # STEP 2 — Coding
    print("\n===== CODER =====\n")

    code = await coder.run(task=planner_output)

    coder_output = code.messages[-1].content

    print(coder_output)

    # STEP 3 — Review
    print("\n===== CRITIC =====\n")

    review = await critic.run(task=coder_output)

    critic_output = review.messages[-1].content

    print(critic_output)

    # STEP 4 — Save generated code
    with open("calculator.py", "w", encoding="utf-8") as f:
        f.write(coder_output)

    print("\n✅ calculator.py saved successfully")

asyncio.run(main())