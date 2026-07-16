def classify_risk(rainfall):
    if rainfall >= 1700:
        return "Low Risk"
    elif rainfall >= 1500:
        return "Moderate Risk"
    else:
        return " High Risk"
