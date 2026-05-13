import streamlit as st
import pandas as pd
import time

from utils.threat_intel import (
    check_abuseipdb,
    check_virustotal
)

from utils.risk_scoring import (
    calculate_risk_score,
    classify_alert
)

from utils.ml_model import (
    detect_anomalies
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI SOC Dashboard",
    layout="wide"
)

st.title("AI SOC Analyst Dashboard")

st.subheader("Real-Time Security Monitoring")

# ---------------- READ LOGS ----------------

logs = pd.read_csv("logs/security_logs.csv")

# Apply ML anomaly detection
logs = detect_anomalies(logs)

# Placeholder for live updates
placeholder = st.empty()

# Store analysis results
analysis_results = []

# Store SOC decisions
soc_decisions = []

# ---------------- REAL-TIME STREAMING ----------------

for i in range(len(logs)):

    current_logs = logs.iloc[:i + 1].copy()

    # Current latest log
    latest_log = current_logs.iloc[-1]

    # Extract values
    current_ip = latest_log["ip"]

    failed_logins = latest_log["failed_logins"]

    data_transfer = latest_log["data_transfer"]

    country = latest_log["country"]

    anomaly = latest_log["anomaly"]

    # ---------------- THREAT INTELLIGENCE ----------------

    abuse_score = check_abuseipdb(current_ip)

    vt_score = check_virustotal(current_ip)

    # ---------------- RISK SCORING ----------------

    risk_score = calculate_risk_score(
        failed_logins,
        data_transfer,
        country,
        abuse_score,
        vt_score
    )

    severity = classify_alert(risk_score)

    # ---------------- ML STATUS ----------------

    ml_status = (
        "Suspicious"
        if anomaly == -1
        else "Normal"
    )

    # ---------------- FINAL SOC DECISION ----------------

    if severity == "HIGH" or anomaly == -1:

        decision = (
            "Escalate to SOC Analyst"
        )

    elif severity == "MEDIUM":

        decision = (
            "Monitor Activity"
        )

    else:

        decision = (
            "No Action Needed"
        )

    # ---------------- SAVE ANALYSIS ----------------

    analysis_results.append({

        "IP": current_ip,

        "AbuseIPDB Score": abuse_score,

        "VirusTotal Detections": vt_score,

        "Risk Score": risk_score,

        "Severity": severity,

        "ML Status": ml_status
    })

    # ---------------- SAVE SOC DECISION ----------------

    soc_decisions.append({

        "IP": current_ip,

        "Severity": severity,

        "ML Status": ml_status,

        "SOC Decision": decision
    })

    # Convert to dataframe
    analysis_df = pd.DataFrame(
        analysis_results
    )

    decision_df = pd.DataFrame(
        soc_decisions
    )

    # ---------------- DASHBOARD ----------------

    with placeholder.container():

        # ==================================================
        # TABLE 1 — RAW SECURITY LOGS
        # ==================================================

        st.subheader("Incoming Security Logs")

        st.dataframe(current_logs)

        # ---------------- METRICS ----------------

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Total Alerts",
                value=len(current_logs)
            )

        high_risk_logs = analysis_df[
            analysis_df["Severity"] == "HIGH"
        ]

        with col2:
            st.metric(
                label="High Risk Alerts",
                value=len(high_risk_logs)
            )

        # ==================================================
        # TABLE 2 — THREAT ANALYSIS
        # ==================================================

        st.subheader(
            "Threat Intelligence & AI Analysis"
        )

        st.dataframe(analysis_df)

        # ==================================================
        # TABLE 3 — SOC DECISION ENGINE
        # ==================================================

        st.subheader(
            "SOC Decision Engine"
        )

        st.dataframe(decision_df)

        # ==================================================
        # CURRENT ALERT SUMMARY
        # ==================================================

        st.subheader("Current Alert Summary")

        col3, col4, col5 = st.columns(3)

        with col3:
            st.metric(
                label="Current IP",
                value=current_ip
            )

        with col4:
            st.metric(
                label="Risk Score",
                value=risk_score
            )

        with col5:
            st.metric(
                label="Severity",
                value=severity
            )

        # ---------------- THREAT STATUS ----------------

        if severity == "HIGH":

            st.error(
                "High Severity Threat Detected"
            )

        elif severity == "MEDIUM":

            st.warning(
                "Medium Severity Threat Detected"
            )

        else:

            st.success(
                "Low Severity Activity"
            )

        # ---------------- ML RESULT ----------------

        if anomaly == -1:

            st.error(
                "ML Model Detected Suspicious Activity"
            )

        else:

            st.success(
                "ML Model: Normal Behavior"
            )

    # ---------------- REAL-TIME DELAY ----------------

    time.sleep(0.2)