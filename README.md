
# 🤖 Sigma-AI – GenAI-Powered Integrated Platform Environment

![Agentic AI](https://img.shields.io/badge/Powered_by-Agentic_AI-blueviolet)
![Context-Aware](https://img.shields.io/badge/Contextual-Recommendations-blue)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange)

**Sigma-AI** is a **GenAI-enabled** Integrated Platform Environment (IPE) that empowers platform engineers by reducing context switching across tools. It integrates observability, root cause analysis (RCA) generation, network analysis, and intelligent insights into a unified interface using vector search, CMDB correlations, and LLM-powered workflows.

---

## Table of Contents

1. [User Interface Overview](#user-interface-overview)
2. [Power of Two Models – Smart Fallback](#power-of-two-models--smart-fallback)
3. [Incident Similarity Search with L2 (Euclidean) Distance](#incident-similarity-search-with-l2-euclidean-distance)
4. [Intelligence Stack](#intelligence-stack)
5. [Project Structure](#project-structure)
6. [System Architecture](#system-architecture)
7. [Installation](#installation)
8. [Configuration](#configuration)
9. [Running the Application](#running-the-application)
10. [Usage](#usage)
11. [Troubleshooting](#troubleshooting)
12. [License](#license)
13. [Acknowledgments](#acknowledgments)

---

## 🖥️ User Interface Overview

![Sigma-AI UI Preview](docs/sigma_ui_preview.jpg)

- 🧠 **Smart Issue Explorer**  
  Convert natural language issues into embeddings and search similar incidents.
- 🧾 **Incident Investigator**  
  Specific incident ID analysis and RCA generation.
- 🧬 **TraceIQ**  
  Analyze logs from APIs using LLMs to suggest fixes.
- 🌐 **NetViz Explorer**  
  Visualize dependencies dynamically with CMDB mapping.
- 💬 **Agentic Chatbot**  
  Interactive assistance for queries and support.

---

## 🔁 Power of Two Models – Smart Fallback

- ⚡ **Primary**: OpenAI GPT-3.5 for RCA generation.
- 🔄 **Fallback**: Hugging Face Mistral 7B.

---

## 📐 Incident Similarity Search with L2 (Euclidean) Distance

Sigma-AI utilizes FAISS for efficient similarity search:

```
distance = sqrt((x₁ - y₁)² + (x₂ - y₂)² + ... + (xₙ - yₙ)²)

squared_distance = Σ(xᵢ - yᵢ)²
```

---

## 🧠 Intelligence Stack

- 🔡 Embedding: `all-MiniLM-L6-v2`
- 🔍 Vector Search Engine: FAISS
- 🧠 LLMs:
  - OpenAI GPT-3.5
  - Hugging Face Mistral 7B
  - LaMini-Flan-T5-783M

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

## 🧱 System Architecture

```
User Input → Embeddings → FAISS → Top-K Incidents → LLM (GPT-3.5/Mistral) → RCA & Suggestions → CR + Logs (CMDB, TraceID)
```

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/sigma-ai.git
cd sigma-ai
pip install -r requirements.txt
```

---

## ⚙️ Configuration

```bash
export OPENAI_API_KEY=your-key
```

---

## 🚀 Running the Application

```bash
streamlit run streamlit_app.py
```

---

## 🎯 Usage

Use the provided tabs and chatbot for comprehensive incident and log management.

---

## 🔧 Troubleshooting

Check API keys, model availability, and API connectivity.

---

## 📄 License

MIT License

---

## 🙏 Acknowledgments

- Hugging Face
- OpenAI
- Streamlit
- FAISS team
