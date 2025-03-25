
# 🤖 Sigma-AI – GenAI-Powered Integrated Platform Environment

![Agentic AI](https://img.shields.io/badge/Powered_by-Agentic_AI-ff69b4)
![Context-Aware](https://img.shields.io/badge/Contextual-Recommendations-blue)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange)

**Sigma-AI** is a GenAI-enabled Integrated Platform Environment (IPE) application that empowers platform engineering teams by combining multiple tool capabilities into a **single intelligent interface**. It reduces context switching, streamlines operations, and introduces **Agentic AI capabilities** like:

- 🔁 Contextual understanding of incidents and system data  
- 💡 Intelligent recommendations based on historical and real-time context  
- 🧠 Root cause analysis using LLMs  
- ✍️ Automated description reframing for better incident clarity  
- 🔍 Extraction of key data points and correlations from change logs, incident history, and trace logs  

---

## 🧠 How It Works

<p align="center">
  <img src="docs/vector_embedding_diagram_750x350.png" alt="Vector Embedding Process" width="750" height="350"/>
</p>

1. **Raw data** (incidents, descriptions, etc.) is embedded into high-dimensional vectors.  
2. FAISS is used for **vector similarity search**.  
3. A connected **LLM generates RCA summaries** from top matching incidents.  
4. Relevant **Change Requests and logs** are correlated automatically.  

---

## 🚀 Features

- 🔍 **Semantic Incident Search**  
- 📊 **Top Matching Incidents**  
- 🧠 **AI-Powered RCA Generation**  
- 🔁 **Change Request Correlation**  
- 📄 **Log Trace Lookup**  

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

## 🤖 LLM Setup

- Embeddings: SentenceTransformers (`all-MiniLM-L6-v2`)
- Vector Store: FAISS
- LLMs: OpenAI GPT-3.5 (primary), Hugging Face Mistral 7B (fallback)

> Set your OpenAI API Key:
```bash
export OPENAI_API_KEY=your-key
```

---

## 📈 Sample Data Schema

**incident_data.csv**
| incident_id | description | resolution | cause | app | app_name | incident_date | trace_id | combined_text |

---

## 🔁 Power of Two Models – Smart Fallback Built In

Sigma-AI is designed to be resilient and flexible with **dual model capability**:

- ⚡ **Primary Model**: OpenAI GPT-3.5 is used for generating deep, contextual RCA and resolution suggestions.
- 🔄 **Fallback Model**: Hugging Face's Mistral 7B (via transformers) is automatically used when OpenAI API limits are hit or credentials are missing.

This smart fallback ensures uninterrupted RCA generation, giving your team consistent insights whether you're using cloud APIs or local models.

---

## 🧱 System Architecture

```
User Input (Incident ID or Free Text)
        |
[Embedding Model: all-MiniLM-L6-v2]
        |
   [Vector Embedding]
        |
FAISS Similarity Search (Euclidean Distance)
        |
Retrieve Top-K Similar Incidents
        |
[LLM: GPT / Mistral]
→ RCA Generation   → Resolution Suggestion
        |
CR + Log Correlation (CMDB + Trace ID)
```

---

## 🤝 How to Contribute

We welcome community contributions to make Sigma-AI better!

1. **Fork** the repository on GitHub  
2. **Clone** your forked repo locally  
3. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and test them  
5. Commit and push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a **Pull Request** on GitHub with a clear description

### 📬 Suggestions / Issues

- Found a bug? [Open an issue](https://github.com/your-repo/issues)  
- Have an idea? Start a discussion or create a feature request!

Let’s build an intelligent future for incident management together 🚀

---

## 📐 Similarity Search with FAISS (Gaussian Distance)

Sigma-AI uses **FAISS** for high-speed vector similarity search. Unlike plain cosine or Euclidean metrics, we employ a **Gaussian similarity kernel** to better capture semantic closeness:

### 🧪 Gaussian Distance Formula

The similarity score **S(x, y)** between two vectors `x` and `y` is calculated as:

```
S(x, y) = exp(-‖x - y‖² / (2 * σ²))
```

Where:
- `‖x - y‖²` is the squared Euclidean distance between embeddings
- `σ` is a tunable scaling parameter (standard deviation of similarity distribution)
- `exp()` applies the Gaussian kernel, giving higher weights to closer vectors

This Gaussian similarity helps us:
- Emphasize highly relevant matches
- Soften sharp cutoffs from raw distance
- Improve retrieval precision, especially with noisy or ambiguous queries

This hybrid technique ensures that incident searches return **semantically meaningful results** even when phrased differently or across noisy operational data.
