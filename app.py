import streamlit as st
import pandas as pd
import time
from utils.threat_intel import (
    check_abuseipdb,
    check_virustotal
)
st.set_page_config(page_title="AI SOC Dashboard", layout="wide")

st.title("AI SOC Analyst Dashboard")

st.subheader("Real-Time Security Monitoring")


# Read CSV logs
logs = pd.read_csv("logs/security_logs.csv")

# Placeholder for dynamic updates
placeholder = st.empty()

# Simulate real-time log streaming
for i in range(len(logs)):
    
    current_logs = logs.iloc[:i+1].copy()
    
         
    current_logs["severity"] = current_logs["failed_logins"].apply(
    lambda x: "High" if x > 10 else "Low"
    )

    with placeholder.container():

        st.write("Incoming Security Alerts")

        st.dataframe(current_logs)

        st.metric(
            label="Total Alerts",
            value=len(current_logs)
        )

        high_risk = current_logs[
            current_logs["failed_logins"] > 10
        ]

        st.metric(
            label="High Risk Alerts",
            value=len(high_risk)
        )
        current_ip = current_logs.iloc[-1]["ip"]

        abuse_score = check_abuseipdb(current_ip)

        vt_score = check_virustotal(current_ip)

    time.sleep(0.002)
st.subheader("Threat Intelligence")

st.write(f"Current IP: {current_ip}")

st.metric(
    label="AbuseIPDB Score",
    value=abuse_score
)

st.metric(
    label="VirusTotal Malicious Detections",
    value=vt_score)