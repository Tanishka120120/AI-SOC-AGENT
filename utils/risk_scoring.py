def calculate_risk_score(
    failed_logins,
    data_transfer,
    country,
    abuse_score,
    vt_score
):

    risk_score = 0

    # Failed login analysis
    if failed_logins > 15:
        risk_score += 40

    elif failed_logins > 7:
        risk_score += 20

    # Large data transfer
    if data_transfer > 5:
        risk_score += 30

    # Suspicious countries
    suspicious_countries = [
        "Russia",
        "China",
        "North Korea"
    ]

    if country in suspicious_countries:
        risk_score += 20

    # Threat reputation
    if abuse_score > 70:
        risk_score += 30

    if vt_score > 5:
        risk_score += 30

    return risk_score


def classify_alert(risk_score):

    if risk_score >= 80:
        return "HIGH"

    elif risk_score >= 40:
        return "MEDIUM"

    else:
        return "LOW"