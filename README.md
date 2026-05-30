# Mindloom

Mindloom is a local first autonomous AI agent framework designed to plan tasks, generate code, execute actions, review results, and iteratively improve solutions.

The project runs entirely on local hardware using Ollama and open source language models.

## Current Features

Local LLM execution through Ollama

Multi agent architecture

Planner agent for task decomposition

Coder agent for code generation

Critic agent for review and feedback

Tool execution system

File creation and modification

Python code execution

Shell command execution

Autonomous task loop

Local operation without cloud APIs

## Architecture

User Request

Planner

Coder

Tool Router

Execution Layer

Critic

Retry Loop

## Project Structure

ai-swarm

main.py

core

tool_router.py

tools

executor.py

workspace

generated files

## Requirements

Windows 11

Python 3.11 or newer

Ollama

Qwen2.5 Coder 14B

AutoGen

32 GB RAM recommended

NVMe SSD recommended

## Current Status

Version 0.3

Implemented

Agent orchestration

Tool execution layer

Local model integration

Basic autonomous workflow

Planned

Memory system

Project workspace management

Multi file project generation

Long running autonomous tasks

Multi agent collaboration

Browser automation

## Installation

Clone repository

Create virtual environment

Install dependencies

Install Ollama

Download Qwen2.5 Coder

Start Ollama

Run main.py

## Vision

Mindloom aims to become a fully autonomous local AI operating system capable of planning, coding, executing, reviewing, and improving software projects independently while remaining fully open source and self hosted.
