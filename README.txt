Here is a **clean Obsidian-ready Markdown playbook** you can copy-paste directly.

---

````md
# 🤖 Local Multi-Agent AI Swarm Playbook (Windows + Ollama)

## 📌 Overview

This playbook explains how to build a **local autonomous multi-agent AI system** using:
- Ollama (local LLM runtime)
- Qwen2.5-Coder 14B
- AutoGen (new agent framework)
- Python (Windows 11 setup)

The system allows:
- Multiple AI agents to communicate
- Plan → Code → Review workflows
- Autonomous project generation
- Local file creation
- Offline AI coding assistant

---

# 🧠 Core Idea

Instead of one AI answering:

> We simulate a **team of AI developers**

Example roles:
- 🧠 Planner → designs solution
- 💻 Coder → writes code
- 🔍 Critic → reviews & improves

They collaborate like a real software team.

---

# 🖥️ Hardware Requirements

## 🟢 Minimum (Works but slower)
- CPU: Intel i5 / i7 (8th gen+)
- RAM: 16 GB
- Storage: 20 GB free SSD
- GPU: Not required (CPU inference)

## 🟡 Recommended (Your setup level)
- CPU: Intel i9 12th Gen ✔
- RAM: 32 GB ✔
- SSD: NVMe ✔
- GPU: Optional

## 🔴 Ideal (Fast local AI)
- GPU: RTX 4090 (24GB VRAM)
- RAM: 64–128 GB
- NVMe SSD: 2TB+

---

# 🧰 Software Requirements

## Must-have tools

### 1. Ollama
Local LLM runtime
```bash
https://ollama.com
````

Install model:

```bash
ollama run qwen2.5-coder:14b
```

---

### 2. Python (Windows)

Install:

```bash
https://www.python.org/downloads/windows/
```

✔ IMPORTANT:

* Enable "Add Python to PATH"

---

### 3. AutoGen (New Version)

Install inside virtual environment:

```bash
pip install pyautogen autogen-ext chromadb watchdog
```

---

# 📁 Project Setup

```bash
mkdir ai-swarm
cd ai-swarm
python -m venv venv
venv\Scripts\activate
```

---

# ⚙️ Core Architecture

```text
User Prompt
   ↓
Planner Agent
   ↓
Coder Agent
   ↓
Critic Agent
   ↓
File Output (Python Project)
```

---

# 🤖 Agent Roles

## 🧠 Planner

* Breaks problem into steps
* Designs architecture

## 💻 Coder

* Writes code
* Implements logic

## 🔍 Critic

* Finds bugs
* Suggests improvements

---

# 🔌 Ollama Integration (IMPORTANT)

Use OpenAI-compatible endpoint:

```python
base_url="http://localhost:11434/v1"
api_key="ollama"
```

---

# ⚠️ Common Setup Issues

## ❌ Problem: ModuleNotFoundError (autogen)

✔ Fix:

```bash
pip install pyautogen
```

---

## ❌ Problem: Model not recognized

✔ Fix:
Add manual model info:

```python
model_info={
    "vision": False,
    "function_calling": False,
    "json_output": False,
    "structured_output": False,
    "family": "unknown",
}
```

---

## ❌ Problem: Agents hang or no output

✔ Fix:

* Reduce model load
* Use CPU-friendly settings
* Avoid parallel execution

---

# 🚀 First Working Script Flow

1. Planner generates plan
2. Coder generates code
3. Critic reviews code
4. Code saved into file

Output file:

```text
calculator.py
```

---

# 🧪 Example Task

```text
Build a Python calculator with:
- add
- subtract
- multiply
- divide
```

System will generate:

* plan
* code
* review
* final file

---

# 💾 File Output System

Generated files stored in:

```text
D:\Projects\ai-swarm\
```

---

# ⚡ Performance Tips

## 🧠 Use sequential agents

Do NOT run many agents in parallel on CPU.

## 🧠 Keep models small

Recommended:

* qwen2.5-coder:14b ✔
* smaller models for speed

## 🧠 Limit context size

Long conversations slow Ollama.

---

# 🧩 Recommended Extensions (Later Stage)

## Memory

* ChromaDB

## Browser automation

* browser-use

## Workflow engine

* LangGraph

## Multi-agent frameworks

* AutoGen
* CrewAI
* MetaGPT

---

# 🧠 Design Principles

✔ Start simple
✔ 3 agents max initially
✔ Sequential execution only
✔ Always save outputs to files
✔ Keep prompts structured

---

# ❗ What NOT to do

❌ Don’t start with 100 agents
❌ Don’t use parallel inference on CPU
❌ Don’t overcomplicate architecture early
❌ Don’t mix AutoGen versions randomly

---

# 🔥 Growth Path

## Stage 1 (Current)

* Planner → Coder → Critic
* File generation

## Stage 2

* Self-improving loop
* Multi-file projects

## Stage 3

* Browser automation
* GitHub integration

## Stage 4

* Fully autonomous coding agent

---

# 🧭 Final Goal

Build a system that:

> Takes one prompt → generates full working software project autonomously

---

# 🧠 Mental Model

Think of it like:

> You are building a small AI software company inside your laptop

Each agent = employee
Each task = project
Ollama = brain
Python = execution layer

---

```
```
