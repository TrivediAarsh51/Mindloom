# 🧠 Mindloom

> Local-First Autonomous Multi-Agent Software Engineering Framework

Mindloom is an experimental autonomous AI software engineering system that runs entirely on local infrastructure using Ollama-hosted open-source language models.

The framework simulates a real software development team by combining multiple specialized AI agents capable of designing, planning, generating, testing, reviewing, and repairing software projects automatically.

---

## 🚀 Current Version

**Mindloom v0.8**

### Highlights

* 🧠 Multi-Agent Architecture
* 🏗 Architecture-Driven Development
* 📋 Automated Planning System
* 💻 Specialized Coding Agents
* ⚙️ Tool-Based Code Execution
* 🧪 Automated Testing Pipeline
* 🔧 Self-Healing Fixer Loop
* 💾 Persistent Project Memory
* 📊 Task Graph Execution Engine
* ⚡ Parallel Task Execution Foundation
* 🔒 Local-Only Operation

---

# 🎯 Vision

Mindloom aims to become a fully autonomous local software engineering system capable of:

* Designing software architectures
* Planning implementation workflows
* Writing production-ready code
* Executing and testing software
* Debugging and repairing failures
* Coordinating multiple AI agents
* Operating entirely offline

No cloud APIs.

No vendor lock-in.

No internet dependency.

---

# 🏛 Architecture

```text
User Request
      │
      ▼
Architect Agent
      │
      ▼
Planner Agent
      │
      ▼
Task Graph
      │
      ▼
Parallel Coder Agents
      │
      ▼
Tool Router
      │
      ▼
Executor Layer
      │
      ▼
Test Runner
      │
      ▼
Critic Agent
      │
      ▼
Fixer Agent
      │
      ▼
Persistent Memory
      │
      ▼
Final Output
```

---

# 🧠 Agent System

## 🏗 Architect Agent

Responsibilities:

* Generate project architecture
* Define system structure
* Design module organization

---

## 📋 Planner Agent

Responsibilities:

* Analyze requirements
* Break work into tasks
* Generate executable task plans

Output Example:

```json
{
  "backend": ["api.py"],
  "core": ["logic.py"],
  "tests": ["test_logic.py"]
}
```

---

## 💻 Coder Agents

Specialized agents responsible for:

### Backend Agent

* APIs
* Services
* Infrastructure code

### Core Agent

* Business logic
* Application functionality

### Test Agent

* Unit tests
* Validation code

---

## 🧪 Test Runner

Responsibilities:

* Execute generated tests
* Capture failures
* Report results

---

## 🧠 Critic Agent

Responsibilities:

* Review generated code
* Detect quality issues
* Suggest improvements

---

## 🔧 Fixer Agent

Responsibilities:

* Analyze failures
* Repair broken code
* Retry execution automatically

---

# ⚙️ Tool System

Mindloom uses a controlled tool-execution architecture.

Agents do not directly modify files.

Instead they emit tool commands.

Example:

```text
TOOL: write_file("backend/api.py", "...")
TOOL: run_python("backend/api.py")
TOOL: run_shell("pytest")
```

Supported Tools:

| Tool         | Purpose                |
| ------------ | ---------------------- |
| write_file() | Create or modify files |
| run_python() | Execute Python scripts |
| run_shell()  | Execute shell commands |

---

# 📂 Project Structure

```text
ai-swarm/
│
├── backend/
│
├── core/
│   ├── architect.py
│   ├── memory.py
│   ├── task_graph.py
│   ├── fixer.py
│   ├── tool_router.py
│   ├── test_runner.py
│   ├── agent_state.py
│   ├── messages.py
│   └── merge_agent.py
│
├── database/
│
├── frontend/
│
├── tests/
│
├── tools/
│   ├── executor.py
│   └── test.py
│
├── workspace/
│   └── project_state/
│       ├── memory.json
│       ├── tasks.json
│       ├── logs.json
│       └── architecture.md
│
├── main.py
│
└── README.md
```

---

# 💾 Memory System

Mindloom stores persistent project information inside:

```text
workspace/project_state/
```

Stored Data:

* Architecture
* Plans
* Generated Code
* Reviews
* Test Results
* Task Status

This allows agents to maintain context throughout execution.

---

# 📊 Task Graph Engine

The TaskGraph system manages execution flow.

Features:

* Task scheduling
* Dependency tracking
* Status management
* Duplicate prevention
* Parallel execution preparation

Task Format:

```text
backend:api.py
core:logic.py
tests:test_logic.py
```

---

# ⚡ Parallel Execution

Mindloom v0.8 introduces the foundation for parallel execution using:

```python
asyncio.gather(...)
```

This allows multiple implementation tasks to execute simultaneously.

Example:

```text
backend/api.py
core/logic.py
tests/test_logic.py
```

can be processed concurrently.

---

# 🔁 Self-Healing Workflow

```text
Generate Code
      │
      ▼
Execute
      │
      ▼
Run Tests
      │
      ▼
Failure?
      │
 ┌────┴────┐
 │   Yes   │
 └────┬────┘
      ▼
 Fixer Agent
      │
      ▼
 Regenerate
      │
      ▼
 Retest
      │
      ▼
 Success
```

The system automatically attempts to repair generated code when failures occur.

---

# 🔒 Local-First Design

Mindloom is designed to run completely offline.

Current setup:

* Ollama
* Qwen2.5-Coder
* Python Runtime

No external APIs are required.

---

# 🖥 Requirements

### Hardware

Recommended:

* Intel i9 (or equivalent)
* 32GB RAM
* SSD Storage
* Dedicated workspace storage

Minimum:

* 16GB RAM
* Modern CPU

---

### Software

* Python 3.11+
* Ollama
* Git

---

# 📦 Installation

Clone repository:

```bash
git clone https://github.com/yourusername/mindloom.git
cd mindloom
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🤖 Start Ollama

Example:

```bash
ollama run qwen2.5-coder:7b
```

or

```bash
ollama run qwen2.5-coder:32b
```

---

# 🚀 Run Mindloom

```bash
python main.py
```

---

# 💡 Example Request

```text
Create a Python calculator project with:

- add
- subtract
- multiply
- divide

Use separate modules and unit tests.
```

Mindloom will:

1. Generate architecture
2. Create implementation plan
3. Generate files
4. Execute tools
5. Run tests
6. Review code
7. Fix failures
8. Produce final output

---

# 🛣 Roadmap

## v0.9

* Worker Pools
* Task Claiming System
* True Swarm Coordination
* Agent Messaging Layer
* Merge Coordination

---

## v1.0

* Autonomous Project Builder
* Long-Term Memory
* Reflection Loops
* Multi-Model Support
* Plugin Ecosystem

---

# ⚠ Current Status

Mindloom v0.8 is an active experimental project.

Current capabilities:

✅ Multi-Agent Workflow

✅ Architecture Generation

✅ Planning System

✅ Task Graph Execution

✅ Tool Execution

✅ Persistent Memory

✅ Automated Testing

✅ Self-Healing Loop

✅ Parallel Task Foundation

Future releases will focus on transforming Mindloom into a true autonomous software engineering swarm.

---

# 📜 License

MIT License

---

# ⭐ Contributing

Contributions, ideas, architecture improvements, and experiments are welcome.

Mindloom is being built as a research-driven autonomous software engineering platform focused on local AI execution.

---

**Mindloom v0.8**
*Building the foundation for autonomous local software engineering.*
