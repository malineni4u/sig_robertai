
# 🤖 Sigma-AI – GenAI-Powered Integrated Platform Environment

![Agentic AI](https://img.shields.io/badge/Powered_by-Agentic_AI-blueviolet?style=for-the-badge&logo=openai&logoColor=white)
![Context-Aware](https://img.shields.io/badge/Contextual-Recommendations-blue)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange)

**Sigma-AI** is a GenAI-enabled Integrated Platform Environment (IPE) that empowers platform engineers by reducing context switching across tools. It brings observability, RCA generation, network analysis, and intelligent insights into a unified interface using vector search, CMDB correlations, and LLM-powered workflows.

---

## 🖥️ Streamlit UI Overview

Sigma-AI presents four core tabs to the user:

### 1. **Smart Issue Explorer**
Enter **any natural language text** related to an issue. Sigma-AI:
- Converts it into vector embeddings
- Uses FAISS with Gaussian Distance to find similar past incidents
- Uses GenAI (LLMs) to provide:
  - Contextual incident matches
  - Relevant RCA suggestions
  - Correlated CRs (Change Requests) based on CI and timing
  - Helpful resolution summaries

### 2. **Incident Investigation**
Focused analysis for a **specific incident ID**. This tab:
- Retrieves historical matches
- Applies LLM to generate a **Root Cause Analysis (RCA)**
- Suggests probable causes and next steps

### 3. **Trace IQ**
For logs and real-time issue traces:
- Reads logs from connected log injection APIs
- Applies LLM to suggest possible fixes
- Helps platform teams derive meaning from complex logs

### 4. **NetViz Explorer**
Network and application visualization tool:
- Builds a **dynamic network diagram** from CMDB data
- Displays app-to-CI/API relationships
- Helps teams understand dependency paths and potential breakpoints

---

## 🧠 Chatbot Assistant

An integrated **Agentic AI-powered chatbot** enables:
- Self-help for generalized platform queries
- Guidance on Sigma-AI usage
- Fast answers to system and RCA-related questions
- Direct interaction with knowledge embedded from your incidents, CRs, and CMDB

---

## 🔁 Power of Two Models – Smart Fallback

Sigma-AI intelligently uses:
- ⚡ **Primary**: OpenAI GPT-3.5 for RCA generation
- 🔄 **Fallback**: Hugging Face Mistral 7B when OpenAI quota limits apply

---

## 📐 Similarity Search with Gaussian Distance

```
S(x, y) = exp(-‖x - y‖² / (2 * σ²))
```

- `‖x - y‖²`: Squared Euclidean distance
- `σ`: Scaling factor
- Returns smooth similarity scores for better ranking precision

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

## 🛠️ Installation

```bash
git clone https://github.com/your-username/sigma-ai.git
cd sigma-ai
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🤝 Contributions

We welcome PRs, ideas, and feedback to improve Sigma-AI for platform teams.

---

Let’s build an intelligent, self-healing future together with Sigma-AI.
