import streamlit as st
import pandas as pd
import time
import plotly.express as px
from fpdf import FPDF

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

from utils.ai_agent import (
    generate_soc_response
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="CyberSentinel AI",
    layout="wide"
)

st.title("IntelliSOC Dashboard")

st.subheader(
    "Real-Time Security Monitoring & Threat Detection"
)

# ==================================================
# LOAD LOGS
# ==================================================

logs = pd.read_csv(
    "logs/security_logs.csv"
)

# Apply ML anomaly detection
logs = detect_anomalies(logs)

placeholder = st.empty()

# ==================================================
# STORAGE VARIABLES
# ==================================================

analysis_results = []
soc_decisions = []
ai_explanations = []

# ==================================================
# PDF REPORT FUNCTION
# ==================================================

def generate_pdf_report(
    ip,
    severity,
    ml_status,
    abuse_score,
    vt_score,
    risk_score,
    decision,
    ai_analysis
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 18)

    pdf.cell(
        200,
        10,
        txt="AI SOC Incident Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)

    pdf.cell(200, 10, txt=f"IP Address: {ip}", ln=True)

    pdf.cell(200, 10, txt=f"Severity: {severity}", ln=True)

    pdf.cell(200, 10, txt=f"ML Status: {ml_status}", ln=True)

    pdf.cell(200, 10, txt=f"AbuseIPDB Score: {abuse_score}", ln=True)

    pdf.cell(200, 10, txt=f"VirusTotal Detections: {vt_score}", ln=True)

    pdf.cell(200, 10, txt=f"Risk Score: {risk_score}", ln=True)

    pdf.cell(200, 10, txt=f"SOC Decision: {decision}", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, txt="AI Threat Analysis", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 11)

    pdf.multi_cell(
        0,
        8,
        txt=ai_analysis
    )

    filename = f"{ip}_incident_report.pdf"

    pdf.output(filename)

    return filename

# ==================================================
# REAL-TIME STREAMING
# ==================================================

for i in range(len(logs)):

    current_logs = logs.iloc[:i + 1].copy()

    latest_log = current_logs.iloc[-1]

    # ==================================================
    # EXTRACT VALUES
    # ==================================================

    current_ip = latest_log["ip"]

    failed_logins = latest_log["failed_logins"]

    data_transfer = latest_log["data_transfer"]

    country = latest_log["country"]

    anomaly = latest_log["anomaly"]

    # ==================================================
    # THREAT INTELLIGENCE
    # ==================================================

    abuse_score = check_abuseipdb(
        current_ip
    )

    vt_score = check_virustotal(
        current_ip
    )

    # ==================================================
    # RISK SCORING
    # ==================================================

    risk_score = calculate_risk_score(
        failed_logins,
        data_transfer,
        country,
        abuse_score,
        vt_score
    )

    severity = classify_alert(
        risk_score
    )

    # ==================================================
    # ML STATUS
    # ==================================================

    if anomaly == -1:

        ml_status = "Suspicious"

    else:

        ml_status = "Normal"

    # ==================================================
    # SOC DECISION LOGIC
    # ==================================================

    if (
        severity == "HIGH"
        and ml_status == "Suspicious"
        and abuse_score > 70
    ):

        decision = (
            "BLOCK IP IMMEDIATELY"
        )

    elif (
        severity == "HIGH"
        or ml_status == "Suspicious"
    ):

        decision = (
            "Escalate to SOC Analyst"
        )

    elif severity == "MEDIUM":

        decision = (
            "Send Security Warning"
        )

    else:

        decision = (
            "No Action Needed"
        )

    # ==================================================
    # AI SOC ANALYSIS
    # ==================================================

    ai_response = generate_soc_response(
        current_ip,
        failed_logins,
        country,
        risk_score,
        severity,
        anomaly
    )

    # ==================================================
    # STORE ANALYSIS
    # ==================================================

    analysis_results.append({

        "IP": current_ip,

        "Failed Logins": failed_logins,

        "Country": country,

        "AbuseIPDB Score": abuse_score,

        "VirusTotal Detections": vt_score,

        "Risk Score": risk_score,

        "Severity": severity,

        "ML Status": ml_status
    })

    # ==================================================
    # STORE DECISIONS
    # ==================================================

    soc_decisions.append({

        "IP": current_ip,

        "Severity": severity,

        "ML Status": ml_status,

        "SOC Decision": decision
    })

    # ==================================================
    # STORE AI REPORTS
    # ==================================================

    ai_explanations.append({

        "IP": f"{current_ip} #{i+1}",

        "Severity": severity,

        "AI Threat Analysis": ai_response,

        "AbuseIPDB Score": abuse_score,

        "VirusTotal Detections": vt_score,

        "Risk Score": risk_score,

        "ML Status": ml_status,

        "SOC Decision": decision
    })

    # ==================================================
    # DATAFRAMES
    # ==================================================

    analysis_df = pd.DataFrame(
        analysis_results
    )

    decision_df = pd.DataFrame(
        soc_decisions
    )

    ai_df = pd.DataFrame(
        ai_explanations
    )

    # ==================================================
    # DASHBOARD
    # ==================================================

    with placeholder.container():

        # ==================================================
        # TOP METRICS
        # ==================================================

        m1, m2, m3, m4 = st.columns(4)

        with m1:

            st.metric(
                "Total Alerts",
                len(current_logs)
            )

        with m2:

            high_alerts = analysis_df[
                analysis_df["Severity"] == "HIGH"
            ]

            st.metric(
                "High Risk Alerts",
                len(high_alerts)
            )

        with m3:

            suspicious = analysis_df[
                analysis_df["ML Status"] == "Suspicious"
            ]

            st.metric(
                "ML Anomalies",
                len(suspicious)
            )

        with m4:

            st.metric(
                "Current Risk Score",
                risk_score
            )

        st.divider()

        # ==================================================
        # SECTION 1
        # ==================================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Incoming Security Logs"
            )

            st.dataframe(
                current_logs,
                width="stretch",
                height=300
            )

        with col2:

            st.subheader(
                "Current Alert Summary"
            )

            s1, s2, s3 = st.columns(3)

            with s1:

                st.metric(
                    "Current IP",
                    current_ip
                )

            with s2:

                st.metric(
                    "Severity",
                    severity
                )

            with s3:

                st.metric(
                    "ML Status",
                    ml_status
                )

            st.markdown("### Threat Status")

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

        st.divider()

        # ==================================================
        # SECTION 2
        # ==================================================

        col3, col4 = st.columns(2)

        with col3:

            st.subheader(
                "Threat Intelligence Analysis"
            )

            threat_df = analysis_df[[

                "IP",

                "AbuseIPDB Score",

                "VirusTotal Detections",

                "Risk Score",

                "Severity"
            ]]

            st.dataframe(
                threat_df,
                width="stretch",
                height=350
            )

        with col4:

            st.subheader(
                "Threat Severity Distribution"
            )

            severity_counts = analysis_df[
                "Severity"
            ].value_counts()

            fig1 = px.pie(
                values=severity_counts.values,
                names=severity_counts.index,
                title="Threat Severity Distribution"
            )

            st.plotly_chart(
                fig1,
                width="stretch"
            )

        st.divider()

        # ==================================================
        # SECTION 3
        # ==================================================

        col5, col6 = st.columns(2)

        with col5:

            st.subheader(
                "Risk Score Trend"
            )

            fig2 = px.line(
                analysis_df,
                y="Risk Score",
                x=analysis_df.index,
                markers=True,
                title="Risk Score Over Time"
            )

            st.plotly_chart(
                fig2,
                width="stretch"
            )

        with col6:

            st.subheader(
                "Threat Activity by Country"
            )

            country_counts = analysis_df[
                "Country"
            ].value_counts()

            fig_country = px.bar(
                x=country_counts.index,
                y=country_counts.values,
                title="Threats by Country"
            )

            st.plotly_chart(
                fig_country,
                width="stretch"
            )

        st.divider()

        # ==================================================
        # SECTION 4
        # ==================================================

        col7, col8 = st.columns(2)

        with col7:

            st.subheader(
                "SOC Decision Engine"
            )

            st.dataframe(
                decision_df,
                width="stretch",
                height=350
            )

        with col8:

            st.subheader(
                "Failed Login Analysis"
            )

            fig3 = px.bar(
                analysis_df,
                x="IP",
                y="Failed Logins",
                color="Severity",
                title="Failed Logins by IP"
            )

            st.plotly_chart(
                fig3,
                width="stretch"
            )

        st.divider()

        # ==================================================
        # AI INCIDENT REPORTS
        # ==================================================

        st.subheader(
            "AI SOC Incident Reports"
        )

        for idx, row in ai_df.iterrows():

            with st.expander(
                f"{row['IP']} | {row['Severity']}"
            ):

                st.write(
                    row["AI Threat Analysis"]
                )

                pdf_file = generate_pdf_report(
                    row["IP"],
                    row["Severity"],
                    row["ML Status"],
                    row["AbuseIPDB Score"],
                    row["VirusTotal Detections"],
                    row["Risk Score"],
                    row["SOC Decision"],
                    row["AI Threat Analysis"]
                )

                with open(
                    pdf_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label=f"Download Report - {row['IP']}",
                        data=file,
                        file_name=pdf_file,
                        mime="application/pdf",
                        key=f"download_{idx}_{i}_{row['IP']}"
                    )

    # ==================================================
    # REAL-TIME DELAY
    # ==================================================

    time.sleep(0.02)