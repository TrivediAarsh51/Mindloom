from autogen_agentchat.agents import AssistantAgent

class FixerAgent:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="Fixer",
            model_client=model_client,
            system_message="""
You are a Fixer Agent.
Your job is to fix broken code based on Critic feedback, Tool errors, and test failures.
You MUST output ONLY TOOL commands to correct the code.
You can modify multiple files if needed.
Do not write explanations, only TOOL commands.
"""
        )

    async def fix(self, code:str, errors:str, review:str, test_results:str=""):
        task_text = f"""
Previous Code:
{code}

Tool Errors:
{errors}

Critic Feedback:
{review}

Test Results:
{test_results}
"""
        result = await self.agent.run(task=task_text)
        return result.messages[-1].content