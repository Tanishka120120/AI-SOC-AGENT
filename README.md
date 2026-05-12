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

# Day 1 — Project Setup & Initial Dashboard

## Work Completed

The first day focused on setting up the development environment and preparing the basic structure of the project.

Tasks completed:

- Created the complete project folder structure
- Connected the project with GitHub using Git
- Setup Python virtual environment
- Installed required libraries and dependencies
- Created the initial Streamlit dashboard
- Added project configuration files

## Outcome

By the end of Day 1, the basic SOC dashboard was successfully running on Streamlit and the development environment was fully configured for further implementation.
<img width="940" height="922" alt="abae77a4-3e9a-46df-913e-78100d00b97b" src="https://github.com/user-attachments/assets/19a24053-59c6-4438-93e4-f587efc30e35" />

---

# Day 2 — Real-Time Security Log Simulation

## Work Completed

The second day focused on simulating how real SOC systems receive and process security logs continuously.

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

# Day 3 — Threat Intelligence Integration

## Work Completed

The third day focused on integrating external threat intelligence services to identify malicious IP addresses.

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
