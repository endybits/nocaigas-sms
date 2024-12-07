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

    sms_content = sms_content.lower()

    for rule in rules:
        if rule["type"] == "regex":
            if re.search(rule["value"], sms_content):
                risk_score += 0.4
                reasons.append(f"Url Sospechosa: {rule['value']}")
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