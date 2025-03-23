import torch
import types
torch.classes.__path__ = types.SimpleNamespace(_path=[])  # 👈 fake a safe ._path attribute

import streamlit as st
from app.data_loader import load_incident_data
from app.vector_search import build_vector_index, retrieve_similar_incidents
from app.model_runner import generate_root_cause_analysis

st.set_page_config(page_title="Incident RCA Assistant", layout="wide")

st.title("🔎 GenAI-powered Incident Analyzer")

DATA_PATH = "data/incident_data.csv"

with st.spinner("Loading data and building vector index..."):
    df = load_incident_data(DATA_PATH)
    index, embeddings, model = build_vector_index(df)

    query = st.text_input("Enter issue or incident number:")

    if query:
        # Treat query as incident ID if exact match found
        incident_row = df[df["incident_id"] == query]
        query_text = (
            incident_row.iloc[0]["combined_text"]
            if not incident_row.empty
            else query
        )

        with st.spinner("Retrieving similar incidents..."):
            similar = retrieve_similar_incidents(query_text, model, index, df)
            st.subheader("Top Similar Incidents:")
            st.dataframe(similar[["incident_id", "description", "resolution", "cause"]])

        st.markdown("### 🔍 Select an Incident for Detailed Review")
        for i, row in similar.iterrows():
            col1, col2 = st.columns([6, 1])
            with col1:
                st.write(f"**{row['incident_id']}** | {row['description']} | {row['cause']}")
            with col2:
                if st.button("Review", key=f"review_{i}"):
                    st.session_state["incident_selected"] = row.to_dict()

        if st.button("Analyze"):
            with st.spinner("Generating Root Cause Analysis..."):
                rca = generate_root_cause_analysis(query_text, similar)
                st.markdown("### 🧠 Probable Root Cause and Resolution")
                st.markdown(rca)


# --- New Imports for CR + Logs ---
from app.change_checker import get_related_changes, load_changes, load_cmdb
from app.log_checker import get_logs_for_trace_id, load_logs

import streamlit as st
import pandas as pd

# --- Load External Data ---
cmdb_df = load_cmdb("data/CMDB_Mapping.csv")
change_df = load_changes("data/change.csv")
logs_df = load_logs("data/Logs_Lookup.csv")

# --- Utility: Display correlation status ---
def correlation_status(days_diff):
    if days_diff <= 1:
        return "🔴 Strong correlation"
    elif days_diff <= 3:
        return "🟠 Partial correlation"
    else:
        return "🟢 All clear"

# --- Streamlit UI Blocks ---

if "incident_selected" in st.session_state:
    incident = st.session_state["incident_selected"]

    with st.expander("🧾 Incident Review (IR)", expanded=True):
        st.write(f"**Incident ID:** {incident['incident_id']}")
        st.write(f"**Description:** {incident['description']}")
        st.write(f"**App:** {incident['app']} ({incident['app_name']})")
        st.write(f"**Date:** {incident['incident_date']}")
        st.write(f"**Cause:** {incident['cause']}")
        st.write(f"**Resolution:** {incident['resolution']}")

    with st.expander("🔁 Change Review (CR)", expanded=False):
        st.write("Looking for related Change Requests...")
        app = incident['app']
        incident_date = incident['incident_date']
        related_crs = get_related_changes(app, incident_date, change_df)

        if related_crs:
            for cr in related_crs:
                cr_date = pd.to_datetime(cr['date'])
                inc_date = pd.to_datetime(incident_date)
                days_diff = abs((inc_date - cr_date).days)
                status = correlation_status(days_diff)
                st.markdown(f"- **{cr['cr_number']}** | `{cr['date']}` | {status}")
        else:
            st.info("No related Change Requests found.")

    with st.expander("📄 Logs Check (LC)", expanded=False):
        trace_id = incident.get("trace_id", "")
        if trace_id:
            logs = get_logs_for_trace_id(trace_id, logs_df)
            if logs:
                st.markdown(f"**Logs for Trace ID: `{trace_id}`**")
                for line in logs:
                    st.code(line)
            else:
                st.info("No logs found for this trace ID.")
        else:
            st.info("No trace ID associated with this incident.")
