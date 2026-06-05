import json
from pathlib import Path
from datetime import datetime
from threading import Lock
from datetime import datetime

STATE_DIR = Path("workspace/project_state")
STATE_DIR.mkdir(parents=True, exist_ok=True)

MEMORY_FILE = STATE_DIR / "memory.json"


class Memory:

    def __init__(self):

        self.lock = Lock()

        if not MEMORY_FILE.exists():
            MEMORY_FILE.write_text("{}")

    def load(self):

        with self.lock:
            return json.loads(MEMORY_FILE.read_text())

    def save(self, data):

        with self.lock:
            MEMORY_FILE.write_text(
                json.dumps(data, indent=4)
                )
   

    def add(self, key, value, agent="system"):
        data = self.load()

        # Ensure memory key is a list
        if key not in data or not isinstance(data[key], list):
            data[key] = []

        data[key].append({
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "value": value
        })

        self.save(data)

    def latest(self, key, default=None):

        data = self.load()

        if key not in data:
            return default

        if not data[key]:
            return default

        return data[key][-1]["value"]

    def history(self, key):

        data = self.load()

        return data.get(key, [])

    def get_all(self):

        return self.load()