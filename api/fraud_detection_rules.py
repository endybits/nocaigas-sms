rules = [
    # Keywords indicating scams
    {"type": "keyword", "value": "ganaste"},
    {"type": "keyword", "value": "urgente"},
    {"type": "keyword", "value": "premio"},
    {"type": "keyword", "value": "felicidades"},
    {"type": "keyword", "value": "gratis"},
    {"type": "keyword", "value": "reclama"},
    {"type": "keyword", "value": "limitada"},
    {"type": "keyword", "value": "exclusivo"},
    {"type": "keyword", "value": "beneficio"},
    {"type": "keyword", "value": "bono"},
    {"type": "keyword", "value": "cuenta bloqueada"},
    {"type": "keyword", "value": "verifica"},
    {"type": "keyword", "value": "ayuda inmediata"},
    {"type": "keyword", "value": "transferencia"},
    {"type": "keyword", "value": "acceso"},
    {"type": "keyword", "value": "alerta"},
    {"type": "keyword", "value": "confirmar"},
    {"type": "keyword", "value": "pagos pendientes"},
    {"type": "keyword", "value": "ganador"},
    {"type": "keyword", "value": "reembolso"},
    {"type": "keyword", "value": "dinero fácil"},
    {"type": "keyword", "value": "gobierno"},
    {"type": "keyword", "value": "oportunidad única"},
    {"type": "keyword", "value": "tarjeta bloqueada"},
    {"type": "keyword", "value": "actualización necesaria"},
    {"type": "keyword", "value": "pago vencido"},
    {"type": "keyword", "value": "promoción exclusiva"},
    {"type": "keyword", "value": "claves confidenciales"},
    {"type": "keyword", "value": "cobros automáticos"},
    
    # Phrases associated with fraud
    {"type": "keyword", "value": "haz clic aquí"},
    {"type": "keyword", "value": "envía tus datos"},
    {"type": "keyword", "value": "acceso inmediato"},
    {"type": "keyword", "value": "verifica tu identidad"},
    {"type": "keyword", "value": "llama ya"},
    {"type": "keyword", "value": "descarga el archivo"},
    {"type": "keyword", "value": "depósito necesario"},
    {"type": "keyword", "value": "actualiza tu información"},
    {"type": "keyword", "value": "solicita tu beneficio"},
    {"type": "keyword", "value": "no compartas este mensaje"},
    
    # Regex for links and suspicious formats
    {"type": "regex", "value": r"\b(bit\.ly|tinyurl\.com|goo\.gl)\b"},
    {"type": "regex", "value": r"https?://\S+"},
    {"type": "regex", "value": r"\b\d{4}-\d{4}-\d{4}\b"},  # Fake card numbers
    {"type": "regex", "value": r"\b(4\d{3}|5[1-5]\d{2})\d{12}\b"},  # Credit card patterns
    {"type": "regex", "value": r"\b\w+@\w+\.\w+\b"},  # Email addresses in messages
    {"type": "regex", "value": r"(PIN|clave|contraseña)\s*\d+"},  # PIN requests
    
    # Suspicious sender rules
    {"type": "sender", "value": "Unregistered"},
    {"type": "sender", "value": "Unknown"},
    {"type": "sender", "value": "+573000000000"},  # Placeholder for suspicious numbers
    {"type": "sender", "value": "Bank"},  # Impersonating banks
    {"type": "sender", "value": "Gobierno"},
    {"type": "sender", "value": "Promocion"},
    {"type": "sender", "value": "Alerta Seguridad"},
    
    # Miscellaneous patterns
    {"type": "keyword", "value": "descarga inmediata"},
    {"type": "keyword", "value": "actualización urgente"},
    {"type": "keyword", "value": "no pierdas esta oportunidad"},
    {"type": "regex", "value": r"\d{10,}"},  # Long sequences of numbers
]