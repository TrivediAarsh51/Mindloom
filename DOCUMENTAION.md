# MINDLOOM v0.8 — COMPLETE TECHNICAL DOCUMENTATION

---

# Project Name

**Mindloom**

Version: **v0.8**

Type: **Local-First Autonomous Multi-Agent Software Engineering Framework**

---

# 1. PROJECT VISION

Mindloom is an autonomous software engineering system designed to simulate a complete software development team using local Large Language Models.

The objective is to allow a user to provide a single software request and have the system:

* Design the architecture
* Create implementation plans
* Generate code
* Execute code
* Run tests
* Review quality
* Fix failures
* Persist knowledge
* Improve output iteratively

without requiring cloud APIs.

The system operates entirely offline using Ollama-hosted models.

---

# 2. CORE PHILOSOPHY

Mindloom follows five principles:

### Local First

No cloud dependency.

Everything runs locally.

---

### Autonomous Development

The system should be capable of building software with minimal human intervention.

---

### Tool-Based Execution

Agents cannot directly modify the system.

Agents must use approved tools.

---

### Self-Healing

Failures trigger automatic correction loops.

---

### Persistent Learning

Generated artifacts are stored for future reasoning.

---

# 3. CURRENT VERSION OVERVIEW (v0.8)

Mindloom v0.8 includes:

* Multi-Agent Workflow
* Architecture Generation
* Planning Agent
* Specialized Coding Agents
* Tool Router
* File Generation
* Python Execution
* Shell Execution
* Automated Testing
* Critic Reviews
* Fixer Loop
* Persistent Memory
* Task Graph Management
* Parallel Task Execution Foundation

---

# 4. TECHNOLOGY STACK

---

## Python 3.11+

Primary implementation language.

Reason:

* Mature ecosystem
* Async support
* Strong subprocess management
* Excellent filesystem APIs

Used For:

* Entire framework implementation

---

## Ollama

Local model serving infrastructure.

Reason:

* Fully offline
* Local inference
* No API costs
* Privacy

Used For:

* Hosting qwen2.5-coder

---

## Qwen2.5-Coder

Primary reasoning and coding model.

Reason:

* Strong coding capabilities
* Good instruction following
* Efficient local deployment

Used For:

* Planning
* Coding
* Reviewing
* Fixing

---

## AutoGen AgentChat

Agent orchestration layer.

Modules:

* AssistantAgent
* Model Clients

Reason:

* Simplifies agent management
* Enables specialized agent roles

---

## AsyncIO

Python concurrency framework.

Reason:

* Foundation for swarm execution

Used For:

* Parallel task execution

---

## JSON

Structured persistence format.

Reason:

* Human readable
* Easily parsed

Used For:

* Memory
* Tasks
* Logs

---

## AST

Python Abstract Syntax Tree.

Reason:

* Safe parsing of tool calls

Used For:

* Tool Router

---

## Pathlib

Filesystem abstraction.

Reason:

* Cleaner path management

Used For:

* Workspace management

---

## Subprocess

Command execution interface.

Reason:

* Run generated code
* Run shell commands

---

# 5. DIRECTORY STRUCTURE

ai-swarm/

backend/
core/
database/
frontend/
tests/
tools/
workspace/

main.py
README.md

---

# 6. CORE SYSTEM COMPONENTS

---

## main.py

Role:

Master orchestrator.

Responsibilities:

* Initialize agents
* Generate architecture
* Execute planning
* Build task graph
* Run parallel execution
* Trigger testing
* Trigger fixing
* Store results

Why It Exists:

Acts as the central nervous system.

---

## core/architect.py

Agent:

Architect Agent

Responsibilities:

* Analyze user request
* Create architecture

Output:

* Project structure
* System design

Purpose:

Separates design from implementation.

---

## core/memory.py

Class:

Memory

Responsibilities:

* Store persistent state
* Retrieve stored data

Storage:

workspace/project_state/memory.json

Methods:

load()
save()
add()
get()

Purpose:

Provides project memory.

---

## core/task_graph.py

Class:

TaskGraph

Responsibilities:

* Store tasks
* Track completion
* Manage dependencies

Storage:

workspace/project_state/tasks.json

Methods:

load()
save()
add_task()
next_task()
complete()

v0.8 Improvements:

* Duplicate task prevention
* Safer task handling

Purpose:

Acts as execution scheduler.

---

## core/tool_router.py

Purpose:

Convert LLM tool commands into executable actions.

Supported Commands:

write_file()
run_python()
run_shell()

Technology:

AST parsing

Reason:

Avoid unsafe eval execution.

---

## tools/executor.py

Purpose:

Actual system interaction layer.

Functions:

write_file()
run_python()
run_shell()

Responsibilities:

* File creation
* Script execution
* Shell execution

Purpose:

Bridge between agents and operating system.

---

## core/test_runner.py

Agent:

Test Runner

Responsibilities:

* Run tests
* Capture failures
* Return structured results

Purpose:

Quality validation layer.

---

## core/fixer.py

Agent:

Fixer Agent

Responsibilities:

* Analyze failures
* Correct code
* Retry generation

Inputs:

* Errors
* Reviews
* Test results

Purpose:

Self-healing mechanism.

---

## core/messages.py

Purpose:

Agent communication structure.

Stores:

* Sender
* Receiver
* Content
* Metadata

Purpose:

Preparation for future swarm communication.

---

## core/agent_state.py

Purpose:

Track agent runtime state.

Stores:

* Status
* Current task
* Activity

Purpose:

Observability layer.

---

## core/merge_agent.py

Purpose:

Future code merge coordination.

Planned Use:

Combine outputs from multiple coding agents.

Purpose:

Required for true swarm architecture.

---

# 7. AGENT SYSTEM

---

## Architect Agent

Responsibilities:

* Generate architecture
* Define project structure

Output:

Architecture document

---

## Planner Agent

Responsibilities:

* Convert request into task list

Output:

JSON

Example:

{
"backend": ["api.py"],
"core": ["logic.py"],
"tests": ["test_logic.py"]
}

Purpose:

Task decomposition.

---

## Backend Coder

Responsibilities:

Backend implementation.

---

## Core Coder

Responsibilities:

Business logic implementation.

---

## Test Coder

Responsibilities:

Test generation.

---

## Critic Agent

Responsibilities:

* Review code
* Identify issues
* Suggest improvements

Purpose:

Quality assurance.

---

## Fixer Agent

Responsibilities:

* Repair failures
* Improve generated code

Purpose:

Autonomous debugging.

---

# 8. TOOL SYSTEM

Agents do not execute code directly.

Instead they output:

TOOL: write_file(...)
TOOL: run_python(...)
TOOL: run_shell(...)

Flow:

Agent
→ Tool Router
→ Executor
→ Operating System

Benefits:

* Safety
* Auditability
* Extensibility

---

# 9. MEMORY SYSTEM

Storage Location:

workspace/project_state/memory.json

Stores:

* Architecture
* Plans
* Generated Code
* Reviews
* Execution Results

Purpose:

Persistent project state.

---

# 10. TASK GRAPH SYSTEM

Storage Location:

workspace/project_state/tasks.json

Task Format:

module:file.py

Examples:

backend:api.py

core:logic.py

tests:test_logic.py

Features:

* Dependency support
* Status tracking
* Duplicate prevention

Purpose:

Execution planning.

---

# 11. EXECUTION PIPELINE

User Request

↓

Architect Agent

↓

Planner Agent

↓

Task Graph

↓

Coder Agents

↓

Tool Router

↓

Executor

↓

Test Runner

↓

Critic Agent

↓

Fixer Agent

↓

Memory Storage

↓

Final Output

---

# 12. SELF-HEALING LOOP

Workflow:

Generate Code

↓

Execute

↓

Run Tests

↓

Failure Detected

↓

Fixer Agent

↓

Regenerate

↓

Retest

↓

Success

Purpose:

Reduce manual debugging.

---

# 13. PARALLEL EXECUTION (v0.8)

Technology:

asyncio.gather()

Purpose:

Run multiple coding tasks simultaneously.

Example:

backend/api.py

core/logic.py

tests/test_logic.py

executed concurrently.

Benefits:

* Faster generation
* Swarm foundation

Current State:

Basic parallel execution.

Future versions will add:

* Worker pools
* Task claiming
* Dynamic scheduling

---

# 14. SECURITY MODEL

No direct eval()

Uses AST parsing.

Tool execution restricted to:

* File writes
* Python execution
* Shell execution

Benefits:

* Reduced risk
* Controlled execution

---

# 15. CURRENT LIMITATIONS

v0.8 still lacks:

* Strict schema enforcement
* Dynamic task claiming
* Agent-to-agent messaging
* Distributed memory
* Merge conflict resolution
* Worker pool scheduling
* Multi-model specialization
* Reflection loops
* Long-term vector memory

---

# 16. ACHIEVEMENTS THROUGH v0.8

Completed:

✓ Local LLM integration

✓ Architecture generation

✓ Planning system

✓ Task graph execution

✓ Multi-agent workflow

✓ Tool execution framework

✓ Persistent memory

✓ Automated testing

✓ Critic reviews

✓ Fixer loop

✓ Parallel task execution foundation

✓ Duplicate task protection

✓ Safer planner validation

✓ Stable task normalization

---

# 17. VERSION STATUS

Mindloom v0.8 represents the transition from:

"Single-Agent Automation"

to

"Structured Multi-Agent Software Engineering"

The framework now possesses the foundational architecture necessary to evolve into a true autonomous local software development swarm system in future releases.

END OF DOCUMENT
