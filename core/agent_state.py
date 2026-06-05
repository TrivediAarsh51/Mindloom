from datetime import datetime


class AgentState:

    def __init__(self):

        self.states = {}

    def update(
        self,
        agent,
        status,
        task=None
    ):

        self.states[agent] = {
            "status": status,
            "task": task,
            "timestamp": datetime.now().isoformat()
        }

    def get_all(self):

        return self.states