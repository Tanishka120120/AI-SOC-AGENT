import requests
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
        return 0