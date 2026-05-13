import random


def check_abuseipdb(ip):

    malicious_ips = {
        "185.23.45.1": 85,
        "91.200.12.5": 92,
        "103.45.67.8": 70
    }

    return malicious_ips.get(ip, random.randint(0, 20))


def check_virustotal(ip):

    malicious_ips = {
        "185.23.45.1": 8,
        "91.200.12.5": 12,
        "103.45.67.8": 5
    }

    return malicious_ips.get(ip, random.randint(0, 2))

'''import requests
import os
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")
ABUSE_API_KEY = os.getenv("ABUSE_API_KEY")


def check_abuseipdb(ip):

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSE_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    try:
        score = data["data"]["abuseConfidenceScore"]
        return score
    except:
        return 0


def check_virustotal(ip):

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "x-apikey": VT_API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    try:
        malicious = data["data"]["attributes"][
            "last_analysis_stats"
        ]["malicious"]

        return malicious

    except:
        return 0'''