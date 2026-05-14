# AI SOC Analyst Dashboard

The AI SOC Analyst Dashboard is a cybersecurity project that simulates how a real Security Operations Center (SOC) works. The system continuously monitors incoming security logs, analyzes suspicious activities, checks threat intelligence sources, and helps identify potential cyber attacks in real time.

This project combines concepts from both Cybersecurity and Artificial Intelligence to create a smart and interactive SOC monitoring system.

---

# Project Objective

The main goal of this project is to build a simplified AI-powered SOC analyst that can assist security teams in monitoring and analyzing suspicious activities more efficiently.

The system is designed to:

- Monitor incoming security logs in real time
- Detect suspicious login attempts and unusual behavior
- Analyze potentially malicious IP addresses
- Integrate external threat intelligence platforms
- Classify alerts based on risk severity
- Help SOC analysts prioritize important threats

---

# Tech Stack

| Component | Technology |
|---|---|
| Dashboard | Streamlit |
| Backend | Python |
| Database | MySQL |
| Threat Intelligence | VirusTotal API, AbuseIPDB API |
| Data Processing | Pandas |
| AI/ML | Scikit-learn |
| Visualization | Matplotlib |
| Version Control | Git & GitHub |

---

# Part 1 — Project Setup & Initial Dashboard

## Work Completed

The first part focused on setting up the development environment and preparing the basic structure of the project.

Tasks completed:

- Created the complete project folder structure
- Connected the project with GitHub using Git
- Setup Python virtual environment
- Installed required libraries and dependencies
- Created the initial Streamlit dashboard
- Added project configuration files

## Outcome

By the end of part 1, the basic SOC dashboard was successfully running on Streamlit and the development environment was fully configured for further implementation.
<img width="940" height="922" alt="abae77a4-3e9a-46df-913e-78100d00b97b" src="https://github.com/user-attachments/assets/19a24053-59c6-4438-93e4-f587efc30e35" />

---

# Part 2 — Real-Time Security Log Simulation

## Work Completed

The second part focused on simulating how real SOC systems receive and process security logs continuously.

Tasks completed:

- Created automated security log generation script
- Generated large sets of simulated SOC logs
- Stored logs in CSV format
- Implemented dynamic log streaming
- Displayed logs continuously on the dashboard

## Features Added

The dashboard now displays:

- Incoming security alerts
- IP addresses
- Failed login attempts
- Data transfer activity
- High-risk alerts

Each generated log contains:
- IP address
- Number of failed logins
- Data transfer size
- Source country

## Outcome

The dashboard now behaves like a real-time SOC monitoring system by continuously streaming and displaying simulated security events dynamically.

---

# Part 3 — Threat Intelligence Integration

## Work Completed

The third part focused on integrating external threat intelligence services to identify malicious IP addresses.

Tasks completed:

- Integrated VirusTotal API
- Integrated AbuseIPDB API
- Created threat intelligence utility module
- Added malicious IP reputation checks
- Displayed threat information on dashboard

## Features Added

The system can now:

- Check whether an IP address is malicious
- Analyze reputation scores
- Detect suspicious IP activity
- Display threat severity levels
- Generate basic threat intelligence alerts

## Threat Intelligence Workflow

Incoming Security Log
        ↓
Extract IP Address
        ↓
Check VirusTotal Reputation
        ↓
Check AbuseIPDB Reputation
        ↓
Generate Threat Score
        ↓
Display Threat Alert

OUTPUT:
<img width="945" height="925" alt="62e6af19-a495-418c-988b-e17beff7ecb8" src="https://github.com/user-attachments/assets/43a1d4ff-f028-48e2-9e64-39970d0dbd11" />
changing data of security logs:
<img width="936" height="948" alt="ff901e56-060a-477e-9732-04f9c002a829" src="https://github.com/user-attachments/assets/e2b9b7de-0959-4493-a5d7-d578b40046c5" />

Part 4 — Hybrid AI Risk Scoring & SOC Decision Engine

On Part 4, the AI SOC Analyst system was upgraded with a hybrid threat detection architecture combining rule-based cybersecurity logic with machine learning-based anomaly detection. A risk scoring engine was developed to classify incoming alerts into low, medium, and high severity levels based on multiple security parameters such as failed login attempts, suspicious geographical locations, abnormal data transfer activity, and threat intelligence scores.

Additionally, an Isolation Forest machine learning model was integrated to identify unusual behavioral patterns and anomalies within the security logs. The dashboard was further enhanced by separating raw security logs, threat intelligence analysis, and SOC response decisions into multiple structured tables, creating a more realistic SOC workflow visualization.

The SOC Decision Engine now automatically generates recommendations such as monitoring suspicious activity or escalating high-risk incidents to a SOC analyst for further investigation.

Features Implemented
Hybrid AI-based threat detection
Rule-based risk scoring engine
Isolation Forest anomaly detection
Severity classification (Low/Medium/High)
Automated SOC decision engine
Separate dashboards for:
Raw security logs
Threat intelligence analysis
SOC response decisions

Part 4 Output
AI-based risk scoring implemented
ML anomaly detection integrated
Automated SOC decision engine created
Hybrid threat analysis dashboard completed
<img width="1600" height="790" alt="2005e10a-e50d-49f8-8687-2e42d4b2d208" src="https://github.com/user-attachments/assets/277c1cd5-d4a7-4081-b636-ada4758738ab" />
<img width="1600" height="817" alt="656a120c-e537-490a-95a6-697080d1c49f" src="https://github.com/user-attachments/assets/dc700ce4-3018-4890-9bd7-f53bab0b2b97" />
<img width="1600" height="807" alt="fbe51ca6-e329-47dd-89d7-44b895aaf158" src="https://github.com/user-attachments/assets/2e9c5aca-2cdc-4fbe-b264-01633f68bf33" />

## Task 5 — AI SOC Analysis & Threat Visualization

* Implemented advanced SOC detection and monitoring features within the dashboard.

* Added a hybrid threat analysis system combining:

  * Rule-based risk scoring
  * Machine learning anomaly detection using Isolation Forest

* Developed an AI-powered incident reporting module that generates short SOC-style threat explanations for suspicious IP addresses.

* Enhanced the SOC Decision Engine to automatically classify activities into:

  * High Risk
  * Medium Risk
  * Low Risk

* Integrated multiple security visualization graphs including:

  * Threat severity distribution
  * Failed login analysis
  * Risk score trends
  * Country-based threat activity analysis

* Improved real-time dashboard monitoring with intelligent threat evaluation and automated alert analysis.

### Outcome

By the end of task 5, the SOC platform was capable of performing intelligent threat detection, AI-assisted incident analysis, anomaly detection, automated SOC decision-making, and real-time security visualization through an interactive dashboard.
<img width="1600" height="798" alt="d95ddccd-e236-43c3-8c93-7d21bacaa9d1" src="https://github.com/user-attachments/assets/d46a67d6-a8a2-47c7-a305-97cdc7f13f36" />
<img width="1600" height="793" alt="e640f0cf-93d4-49b0-bce6-7d0e93e0e0f8" src="https://github.com/user-attachments/assets/5bd9cc46-3604-4b7d-8dd6-f846668bf98c" />
<img width="1600" height="769" alt="d86a7f16-e7fe-4911-a44d-68a00cd3824e" src="https://github.com/user-attachments/assets/e61be615-f76f-4025-8e6c-15da7dc7a0b5" />
<img width="1600" height="785" alt="05dd7493-08fa-44c3-8660-9ed58a228ac4" src="https://github.com/user-attachments/assets/fb703626-3bc2-4129-b8c4-51da985315f2" />
<img width="1600" height="795" alt="005151f8-69e4-4686-8d88-e7c3754291b7" src="https://github.com/user-attachments/assets/df8087d1-562f-4a1c-9b3d-dd1cde50419d" />
<img width="1600" height="718" alt="a03075e5-50d3-496b-a1b0-0f8f00a6012c" src="https://github.com/user-attachments/assets/c2786f19-5f01-494a-b137-4b7cb767490e" />
<img width="1600" height="613" alt="317ab98a-8c20-4faf-b43f-2763a36502bb" src="https://github.com/user-attachments/assets/7fa7fdf5-5fb9-4728-b51d-b24ef54800cf" />

