# OneTouch.AI

> A voice-first personal AI assistant that interprets natural-language commands and translates them into system-level automation workflows.

OneTouch.AI is a Python-based personal AI action engine designed to unify human-computer interaction through a single conversational interface. By eliminating manual application navigation and repetitive GUI tasks, the platform allows users to execute complex digital workflows using natural text or speech inputs.

---

## Technical Overview

OneTouch.AI integrates automatic speech recognition (ASR), local Large Language Models (LLMs), intent classification, and automation scripts into a responsive, centralized interface. 

For instance, rather than manually launching a messaging platform and locating a contact, a user can input:

> "Message Geethika hi"

The underlying engine parses the command into a structured JSON payload and routes it to the designated automation controller.

### Core Architecture Pipeline

```text
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

---

## Core Capabilities

* **Multimodal Input Support:** Handles both real-time voice streaming and manual text command entry.
* **Deterministic Intent Classification:** Leverages fine-tuned prompting strategies to extract intents, parameters, and entities from unstructured syntax.
* **Localized LLM Inference:** Deploys Ollama with Llama 3.2 locally to process data with low latency and complete offline security.
* **Cross-Application Routing:** Features operational modules for WhatsApp messaging, SMTP email client handling, dialer actions, media playback, and programmatic web queries.
* **Dynamic Entity Resolution:** Matches spoken names against a structured local contact database to map user commands to specific system endpoints.
* **Modern Web Interface:** Built on a responsive Streamlit architecture optimized for clean user interactions.

---

## Project Structure

```text
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
├── requirements.txt
│       └── Monitored Python package dependencies
│
├── .gitignore
│       └── System and environment exclusions for version control
│
└── README.md
        └── Comprehensive technical documentation
```

---

## Execution Methodology

### 1. Command Ingestion
The system accepts raw conversational input via the user interface.
* Sample Input: `Message Geethika hi`

### 2. Speech Processing
When utilizing audio input, the voice processing module utilizes the SpeechRecognition framework to transform acoustic data into normalized text strings.

### 3. Intent Extraction
The text string is fed directly to the local intent engine. The LLM acts as a zero-shot parser, returning a structured data object:

```json
{
  "intent": "whatsapp",
  "recipient": "Geethika",
  "detail": "hi"
}
```

### 4. Downstream Automation
The automation engine reads the structured payload, instantiates the required sub-process or API call, and passes the parameters directly to the target system application handler.

---

## System Configuration and Deployment

### Technical Prerequisites

Ensure your host environment meets the following specifications:
* Python 3.8 or higher
* Git version control system
* Ollama local model provider runtime

### 1. Repository Initialization
Clone the repository and navigate to the project root directory:
```bash
git clone https://github.com/YOUR_USERNAME/OneTouch_AI.git
cd OneTouch_AI
```

### 2. Environment Isolation
Create and activate an isolated virtual environment to manage dependencies securely:
```powershell
# Windows Environment Setup
python -m venv venv
.\venv\Scripts\activate

# Unix/macOS Environment Setup
python3 -m venv venv
source venv/bin/activate
```

### 3. Dependency Provisioning
Install all required libraries specified in the manifest:
```bash
pip install -r requirements.txt
```

### 4. Local Model Provisioning
Download and initialize the lightweight Llama 3.2 model via the Ollama CLI:
```bash
ollama pull llama3.2
```

---

## Running the Application

Execute the Streamlit server to deploy the local web application:

```bash
python -m streamlit run app.py
```

Once running successfully, the platform can be accessed via your web browser at the default local loopback address:
```text
http://localhost:8501
```

---

## Architecture Design Principles

### Security and Data Privacy
OneTouch.AI enforces a strict local-first paradigm. By running Llama 3.2 locally through Ollama, all speech-to-intent operations are executed entirely on the host machine. This design prevents corporate data exfiltration and removes third-party API dependencies.

*Note: Never commit private contact data, access tokens, or sensitive environment variables to the public repository.*

### Current State and Scope
This system is an active prototype. It acts as an orchestrator that accurately detects intents and hands over control to system application links and native UI components. The immediate roadmap focuses on replacing these application handlers with fully headless API integrations and background processing.

---

## Future Roadmap

* **Comprehensive Calendar Integration:** Support for programmatic appointment tracking and chronological scheduling.
* **Native API Orchestration:** Direct IMAP/SMTP and Graph API endpoints for headless email and messaging automation.
* **Advanced Multi-Turn Intent Detection:** Context-aware memory storage allowing the model to handle conversational context across multiple commands.
* **Autonomous Task Planning:** Integration of autonomous AI agent loops capable of breaking down complex, multi-step requests into sequential actions.
* **Bi-directional Audio Loops:** Text-to-Speech (TTS) integration to deliver real-time spoken status updates to the user.

---

## Professional Profile

**Hasini Akula**  
Bachelor of Technology — Computer Science & Engineering  

**Technical Focus Areas:**  
* Artificial Intelligence and Machine Learning Engineering  
* Generative AI Architectures and Prompt Engineering  
* Programmatic Process Automation and Scripting  
* Local LLM Deployment and Optimization Pipelines  
