from transformers import pipeline
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ Use a better CPU-friendly model
hf_model = pipeline(
    "text2text-generation",
    model="MBZUAI/LaMini-Flan-T5-783M",
    device=-1  # CPU
)

client = OpenAI(api_key=openai_api_key)

def huggingface_generate_response(prompt):
    print("🔄 Generating response using Hugging Face model...")
    truncated = prompt[:1100]  # LaMini is more compact, this is usually enough
    result = hf_model(
        truncated,
        max_length=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    output = result[0]['generated_text'].strip()
    return remove_repetitions(output)

def remove_repetitions(text):
    lines = text.splitlines()
    seen = set()
    clean_lines = []
    for line in lines:
        if line.strip() not in seen:
            clean_lines.append(line)
            seen.add(line.strip())
    return "\n".join(clean_lines)

def generate_root_cause_analysis(query, similar_df):
    summary = "\n".join([
        f"Incident {row['incident_id']}: {row['description']} | Resolution: {row['resolution']} | Cause: {row['cause']}"
        for _, row in similar_df.head(3).iterrows()
    ])

    if len(summary) > 800:
        summary = summary[:800] + "..."

    few_shot_example = """
Example:

Issue:
Intermittent connectivity to backend

Similar Incidents:
Incident INC1234: DNS failure | Resolution: Restarted DNS pod | Cause: DNS misconfiguration  
Incident INC1235: Timeout errors | Resolution: Increased timeout | Cause: Network congestion  
Incident INC1236: API failures | Resolution: Rebooted backend | Cause: stale routing table

---
**Probable Root Cause**:
Backend connectivity was failing due to a combination of stale DNS and unoptimized routing paths under network congestion.

**Resolution Plan**:
1. Restart backend and DNS-related pods to refresh stale entries.
2. Validate and update routing table configurations.
3. Monitor traffic load and implement timeout threshold adjustments.

**Preventive Suggestions**:
1. Set up alerts for increased packet drops or timeout errors.
2. Automate stale route detection via periodic probes.
---
"""

    prompt = f"""
You are a highly skilled SRE assistant. Based on the following issue and similar incidents, infer the root cause, recommend a 3-step resolution plan, and provide 2 preventive suggestions.
Even if individual incidents differ slightly, identify any **common failure patterns** that could explain the issue. Avoid rejecting incidents unless they are clearly unrelated.

Your output should **not copy any one incident**. Look for patterns and summarize.

{few_shot_example}

Now apply the same logic to this:

### Issue:
{query}

### Similar Incidents:
{summary}

Respond in the same format as the example:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"⚠️ OpenAI call failed: {e}")
        print("⏪ Falling back to Hugging Face model...")
        return huggingface_generate_response(prompt)