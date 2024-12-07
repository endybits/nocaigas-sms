import re

from api.fraud_detection_rules import rules


def detect_fraud(sms_content, sender, message_id, rules = rules):
    """
    Analizes an SMS message for potential fraud indicators based on a set of rules.

    Args:
        sms_content (str): The content of the SMS message.
        sender (str): The sender of the SMS message.
        rules (list): A list of rules to check against the SMS message.
    
    Returns:
        dict: A dictionary containing the risk score, classification, and reasons for the score.
    """

    risk_score = 0
    reasons = []
    extracted_urls = []

    sms_content = sms_content.lower()

    for rule in rules:
        if rule["type"] == "regex":
            matches = re.findall(rule["value"], sms_content)
            if matches:
                risk_score += 0.4
                for match in matches:
                    if "://" in rule["value"] or rule["value"] == r"https?://\S+":
                        extracted_urls.append(match)
                    reasons.append(f"Url Sospechosa: {match}")
        elif rule["value"] in sms_content and rule["type"] == "keyword":
            risk_score += 0.3
            reasons.append(f"Keyword: {rule['value']}")
        elif rule["value"] in sender and rule["type"] == "sender":
            risk_score += 0.5
            reasons.append(f"Emisor sospechoso: {rule['value']}")
    
    # Determine the classification based on the risk score
    if risk_score >= 0.7:
        classification = "Fraudulento"
    elif risk_score >= 0.4:
        classification = "Sospechoso"
    else:
        classification = "Seguro"
    
    return {
        "risk_score": risk_score if risk_score < 1 else 0.99,
        "classification": classification,
        "reasons": reasons,
        "message_id": message_id
    }