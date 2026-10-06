# OneTouch.AI

> A voice-first personal AI assistant that interprets natural-language commands and converts them into actionable automation workflows.

OneTouch.AI is a Python-based personal AI action assistant designed to simplify human-computer interaction through a unified conversational interface.

Instead of manually navigating between different applications, users can provide commands through **voice or text**. The system analyzes the command, identifies the user's intent, extracts relevant information, and routes the request to the appropriate automation module.

For example:

> "Message Geethika hi"

is converted into a structured intent containing the requested action, recipient, and message.

---

## Technical Overview

OneTouch.AI combines **speech recognition, local Large Language Model (LLM) inference, natural-language intent detection, contact resolution, and application automation** into a centralized Streamlit interface.

The system follows a modular pipeline:

```text
┌─────────────────────────────┐
│      Voice / Text Input     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Speech-to-Text         │
│      (Voice Input)          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Intent Engine         │
│     Ollama + Llama 3.2      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Structured Intent       │
│           JSON              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Contact Resolution &     │
│    Automation Controller    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Target Action         │
└─────────────────────────────┘
