# 🧠 Mindloom

Mindloom is a local-first autonomous AI multi-agent framework designed to plan, design, generate, execute, test, and iteratively improve software projects using open-source LLMs.

It runs fully locally using Ollama and supports a multi-agent engineering workflow that simulates a real software development team.

---

## 🚀 Current Version: v0.7

Mindloom v0.7 introduces:

- 🧠 **Multi-agent AI system** (Planner, Coder, Critic, Fixer, Test Runner)  
- 🔁 **Self-healing code loop** (auto-fix broken code)  
- 🧪 **Automated test execution system**  
- 📁 **Multi-file project generation**  
- ⚙️ **Tool-based execution system** (write/run files, shell commands)  
- 🏗 **Architecture-driven development flow**  
- 💾 **Persistent memory + task graph execution**  

---

## 🧩 Architecture

User Request
↓
Architect Agent
↓
Planner Agent
↓
Parallel Coder Agents (v0.8+ expansion ready)
↓
Tool Execution Layer
↓
Test Runner
↓
Critic Agent
↓
Fixer Agent (self-healing loop)
↓
Final Output


---

## 🧠 Agents

### 🏗 Architect Agent
- Generates system architecture  
- Defines project structure  

### 📋 Planner Agent
- Breaks user request into structured tasks  

### 💻 Coder Agent(s)
- Generates code using TOOL commands only  
- Can create and modify multiple files  

### 🧪 Test Runner
- Executes test files inside workspace  
- Validates generated code  

### 🧠 Critic Agent
- Reviews code quality, structure, and logic  

### 🔧 Fixer Agent
- Fixes broken code based on:  
  - Tool errors  
  - Test failures  
  - Critic feedback  

---

## ⚙️ Features

- ✔ **Autonomous Code Generation**  
  Mindloom can generate full projects from a single prompt.  

- ✔ **Tool-Based Execution**  
  Supports:
  - File creation  
  - Code execution  
  - Shell commands  

- ✔ **Self-Healing Loop**  
  Automatically retries and fixes broken code until success.  

- ✔ **Multi-File Projects**  
  Supports structured project generation instead of single scripts.  

- ✔ **Persistent Memory**  
  Stores:
  - Architecture  
  - Plans  
  - Generated code  
  - Test results  
  - Reviews  

---

## 📁 Project Structure

ai-swarm/
│
├── main.py
├── README.md
│
├── core/
│ ├── architect.py
│ ├── memory.py
│ ├── task_graph.py
│ ├── tool_router.py
│ ├── fixer.py
│ └── test_runner.py
│
├── tools/
│ ├── executor.py
│ └── test.py
│
├── workspace/
│ ├── project_state/
│ │ ├── memory.json
│ │ ├── tasks.json
│ │ ├── architecture.md
│ │ └── logs.json
│ └── generated projects/

## 🧪 Requirements

- Python 3.11+
- Windows 10/11 (or Linux)
- Ollama installed
- Model: qwen2.5-coder:32b (or similar)
- 16GB+ RAM recommended (32GB preferred)

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Run Locally

#### Start Ollama:

```bash
ollama run qwen2.5-coder:32b
```

#### Run Mindloom:

```bash
python main.py
```

---

## 🧪 Example Usage

Run Mindloom:

```bash
python main.py
```

> [!Example Prompt:]
>
> Create a Python calculator project with:
> - add, subtract, multiply, divide
> - separate modules
> - unit tests


## 🔁 Execution Flow

- Architecture is generated
- Plan is created
- Code is generated (possibly multi-file)
- TOOL commands are executed
- Tests are run automatically
- Critic reviews output
- Fixer resolves issues (loop until success)

## 🧠 Vision

Mindloom aims to become a fully autonomous local AI software engineering system, capable of:

- Designing software systems
- Writing production-ready code
- Testing and debugging automatically
- Improving itself over time
- Running completely offline


