import json
from pathlib import Path

STATE_DIR = Path("workspace/project_state")
STATE_DIR.mkdir(parents=True, exist_ok=True)

MEMORY_FILE = STATE_DIR / "memory.json"

class Memory:
    def __init__(self):
        if not MEMORY_FILE.exists():
            MEMORY_FILE.write_text("{}")

    def load(self):
        return json.loads(MEMORY_FILE.read_text())

    def save(self, data):
        MEMORY_FILE.write_text(json.dumps(data, indent=4))

    def add(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def get(self, key, default=None):
        return self.load().get(key, default)