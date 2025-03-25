
# 🤖 GenAI-Powered Integrated Platform Environment

![Agentic AI](https://img.shields.io/badge/Powered_by-Agentic_AI-blueviolete)
![Context-Aware](https://img.shields.io/badge/Contextual-Recommendations-blue)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange)

**Sigma-AI** is a **GenAI-enabled** Integrated Platform Environment (IPE) that empowers platform engineers by reducing context switching across tools. It brings observability, RCA generation, network analysis, and intelligent insights into a unified interface using vector search, CMDB correlations, and LLM-powered workflows.

---

## Table of Contents

1. [Steamlit UI Overview](#User-Interface)
1. [Prerequisites](#prerequisites)
2. [Modesl](#Power)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Features](#features)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)
8. [LLM & Intelligence Stack](#llm--intelligence-stack)
9. [System Architecture](#system-architecture)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)

---

## 🖥️ User-Interface Overview

---

- 🧠 **Smart Issue Explorer**  
  Convert any natural language issue into vector embeddings and search similar incidents. Get RCA and related CRs powered by LLMs. 
    - Converts it into vector embeddings
    - Uses FAISS with Gaussian Distance to find similar past incidents
    - Uses GenAI (LLMs) to provide:
      - Contextual incident matches
      - Relevant RCA suggestions
      - Correlated CRs (Change Requests) based on CI and timing
      - Helpful resolution summaries 
  
- 🧾 **Incident Investigator**  
  Enter a specific incident ID to generate contextual RCA, show related CRs, and suggest resolution.  
    - Retrieves historical matches
    - Applies LLM to generate a **Root Cause Analysis (RCA)**
    - Suggests probable causes and next steps
  
- 🧬 **TraceIQ**  
  Feed logs from APIs, analyze them using LLMs, and receive suggestions based on trace ID and log content.  
    - Reads logs from connected log injection APIs
    - Applies LLM to suggest possible fixes
    - Helps platform teams derive meaning from complex logs

- 🌐 **NetViz Explorer**  
  Visualize app-to-CI/API dependencies using CMDB mapping and explore how components are connected.  
    - Builds a **dynamic network diagram** from CMDB data
    - Displays app-to-CI/API relationships
    - Helps teams understand dependency paths and potential breakpoints
  
- 💬 **Agentic Chatbot**  
  Ask questions, explore suggestions, and receive guidance directly through an LLM-powered assistant.
  - Self-help for generalized platform queries
  - Guidance on Sigma-AI usage
  - Fast answers to system and RCA-related questions
  - Direct interaction with knowledge embedded from your incidents, CRs, and CMDB

---

---

## 🔁 Power of Two Models – Smart Fallback

Sigma-AI intelligently uses:
- ⚡ **Primary**: OpenAI GPT-3.5 for RCA generation
- 🔄 **Fallback**: Hugging Face Mistral 7B when OpenAI quota limits apply

---

## 📐 Incident Similarity Search with Gaussian Distance

```
S(x, y) = exp(-‖x - y‖² / (2 * σ²))
```

- `‖x - y‖²`: Squared Euclidean distance
- `σ`: Scaling factor
- Returns smooth similarity scores for better ranking precision

---

## 🧠 Intelligence Stack

Sigma-AI brings together multiple components to power its intelligence:

- 🔡 **Embedding Model**: `all-MiniLM-L6-v2` from SentenceTransformers  
  Used to convert natural language text into dense vector representations

- 🔍 **Vector Search Engine**: FAISS  
  Performs high-speed similarity search using Gaussian Distance metric

- 🧠 **LLMs (Large Language Models)**:
  - **Primary**: OpenAI GPT-3.5 – Used for contextual RCA generation and suggestions
  - **Fallbacks**:
    - Hugging Face's **Mistral 7B**
    - `LaMini-Flan-T5-783M` – A compact and CPU-friendly open model for generating resolution summaries

This hybrid architecture ensures the platform remains responsive, explainable, and works even in limited environments without internet or API access.

---

## 📂 Project Structure

```
.
├── streamlit_app.py
├── app/
│   ├── data_loader.py
│   ├── vector_search.py
│   ├── model_runner.py
│   ├── change_checker.py
│   └── log_checker.py
├── data/
│   ├── incident_data.csv
│   ├── change.csv
│   ├── CMDB_Mapping.csv
│   └── Logs_Lookup.csv
└── requirements.txt
```

---

## System Architecture

```
User Input (Incident ID or Free Text)
        |
[Embedding Model: all-MiniLM-L6-v2]
        |
   [Vector Embedding]
        |
FAISS Similarity Search (Gaussian Distance)
        |
Retrieve Top-K Similar Incidents
        |
[LLM: GPT / Mistral]
→ RCA Generation   → Resolution Suggestion
        |
CR + Log Correlation (CMDB + Trace ID)
```

---

## LLM & Intelligence Stack

- 🔡 **Embedding**: `all-MiniLM-L6-v2` via SentenceTransformers
- 🔍 **Vector DB**: FAISS with **Gaussian Distance**  
  ```
  S(x, y) = exp(-‖x - y‖² / (2 * σ²))
  ```
- 🧠 **LLMs**:
  - OpenAI GPT-3.5 (Primary)
  - Mistral 7B (Hugging Face fallback)
  - `LaMini-Flan-T5-783M` (lightweight fallback)

---


---

## Installation

```bash
git clone https://github.com/your-username/sigma-ai.git
cd sigma-ai
pip install -r requirements.txt
```

---

## Configuration

### OpenAI API
Set your OpenAI API key in the environment:
```bash
export OPENAI_API_KEY=your-key
```

---

## Running the Application

```bash
streamlit run streamlit_app.py
```

---



## Usage

1. Use **Smart Issue Explorer** to describe symptoms or paste incident text.
2. Use **Incident Investigator** to explore a specific incident ID.
3. Use **TraceIQ** to explore logs by trace ID.
4. Use **NetViz Explorer** to explore visual relationships between services and CIs.
5. Use the built-in chatbot for self-help queries.

---

## Troubleshooting

- Ensure OpenAI API key is correctly set.
- For Hugging Face models, ensure you have internet access or install models locally.
- If logs fail to load, verify log injection API is connected.

---





## License

MIT License

---

## Acknowledgments

- Hugging Face
- OpenAI
- Streamlit
- FAISS team
