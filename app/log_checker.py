
import pandas as pd

def load_logs(logs_path):
    return pd.read_csv(logs_path)

def get_logs_for_trace_id(trace_id, logs_df):
    if not trace_id:
        return []
    logs = logs_df[logs_df["trace_id"] == trace_id]
    return logs["log"].tolist()
