The project tree has been updated to remove both .gitignore and README.md from your directory map, reflecting only the core executable files and dependencies.
Here is the corrected code block for your documentation:

# OneTouch.AI> A voice-first personal AI assistant that interprets natural-language commands and translates them into system-level automation workflows.

OneTouch.AI is a Python-based personal AI action engine designed to unify human-computer interaction through a single conversational interface. By eliminating manual application navigation and repetitive GUI tasks, the platform allows users to execute complex digital workflows using natural text or speech inputs.
---## Technical Overview
OneTouch.AI integrates automatic speech recognition (ASR), local Large Language Models (LLMs), deterministic intent classification, and automation scripts into a responsive, centralized interface. 

For instance, rather than manually launching a messaging platform and locating a contact, a user can input:
> "Message Geethika hi"

The underlying engine parses the command into a structured JSON payload and routes it to the designated automation controller.
### Core Architecture Pipeline```text
[ Voice / Text Command ]
            │
            ▼
 [ Speech-to-Text Engine ]
            │
            ▼
[ Intent Detection Layer ]
            │
            ▼
  [ Local LLM Pipeline ] (Ollama / Llama 3.2)
            │
            ▼
  [ Structured Payload ]
            │
            ▼
 [ System Automation Controller ]
            │
            ▼
    [ Target Action ]
```
---## Core Capabilities* **Multimodal Input Support:** Handles both real-time voice streaming and manual text command entry.* **Deterministic Intent Classification:** Leverages fine-tuned prompting strategies to extract intents, parameters, and entities from unstructured syntax.* **Localized LLM Inference:** Deploys Ollama with Llama 3.2 locally to process data with low latency and complete offline security.* **Cross-Application Routing:** Features operational modules for WhatsApp messaging, SMTP email client handling, dialer actions, media playback, and programmatic web queries.* **Dynamic Entity Resolution:** Matches spoken names against a structured local contact database to map user commands to specific system endpoints.* **Modern Web Interface:** Built on a responsive Streamlit architecture optimized for clean user interactions.
---## Project Structure```text
OneTouch_AI/
│
├── app.py
│       └── Streamlit dashboard and UI rendering layer
│
├── intent_engine.py
│       └── Natural-language parsing and LLM orchestration
│
├── automation_actions.py
│       └── Execution modules for handling downstream application tasks
│
├── contacts.py
│       └── Contact database schema and algorithmic name matching
│
├── voice_input.py
│       └── Audio capture and Speech-to-Text (STT) processing
│
├── main.py
│       └── Core application initialization logic
│
└── requirements.txt
        └── Monitored Python package dependencies
```
---## Intent Analysis Engine Architecture
The core intelligence of OneTouch.AI resides within the intent processing engine, engineered to reliably map arbitrary string inputs into uniform database schemas. The engine utilizes a multi-layered classification strategy to ensure maximum uptime and operational resilience.
### 1. Zero-Shot StructuringThe system transmits raw input commands to a local Llama 3.2 deployment configured with deterministic system constraints. The LLM acts as an isolated zero-shot parser, transforming unstructured communication strings directly into strongly typed schemas:
```json
{
  "intent": "whatsapp",
  "recipient": "Geethika",
  "detail": "hi"
}
```
### 2. Deflation Guardrails & Ingestion ParsingBecause raw LLM text streams are prone to occasional syntax variance (such as text padding or Markdown envelope blocks), the processing framework strips system markdown artifacts programmatically before validating structural state integrity. Missing structural keys are automatically populated using object default policies (`intent: unknown`, `recipient: none`, `detail: none`) to eliminate unhandled downstream execution faults.
### 3. Keyword Sub-process FallbackIn scenarios where hardware constraints or language nuances trigger an inference exception or output an unclassified intent, the application engages a high-performance regex/keyword fallback array. This guarantees system dependability for standard operations (`whatsapp`, `email`, `call`, `music`, `search`) even in an offline or degraded LLM execution state.
---## Architecture Design Principles### Security and Data PrivacyOneTouch.AI enforces a strict local-first paradigm. By running Llama 3.2 locally through Ollama, all speech-to-intent operations are executed entirely on the host machine. This design prevents corporate data exfiltration and removes third-party API dependencies.
### Current State and ScopeThis system is an active prototype. It acts as an orchestrator that accurately detects intents and hands over control to system application links and native UI components. The immediate roadmap focuses on replacing these application handlers with fully headless API integrations and background processing.
---## Future Roadmap* **Comprehensive Calendar Integration:** Support for programmatic appointment tracking and chronological scheduling.* **Native API Orchestration:** Direct IMAP/SMTP and Graph API endpoints for headless email and messaging automation.* **Advanced Multi-Turn Intent Detection:** Context-aware memory storage allowing the model to handle conversational context across multiple commands.* **Autonomous Task Planning:** Integration of autonomous AI agent loops capable of breaking down complex, multi-step requests into sequential actions.* **Bi-directional Audio Loops:** Text-to-Speech (TTS) integration to deliver real-time spoken status updates to the user.

Is there any other architectural detail you want to add to this README, or should we move on to testing or optimizing your main application files?

