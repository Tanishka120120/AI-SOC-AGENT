
import google.generativeai as genai

genai.configure(
    api_key="AIzaSyD_5rkl3U9D1TkF7sg_jOLafyxS3UfuJ9I"
)

model = genai.GenerativeModel(
    "gemini-3.1-flash-lite"
)

def generate_soc_response(
    ip,
    failed_logins,
    country,
    risk_score,
    severity,
    anomaly
):

    prompt = f"""
    You are an expert SOC Analyst.

    Analyze this cybersecurity event.

    IP Address: {ip}
    Failed Logins: {failed_logins}
    Country: {country}
    Risk Score: {risk_score}
    Severity: {severity}
    ML Anomaly Status: {anomaly}

    Generate a professional SOC incident report.

    Include:
    1. Threat Summary
    2. Why activity is suspicious
    3. Recommended remediation

    Keep response concise and structured.
    """

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"AI analysis unavailable: {e}"