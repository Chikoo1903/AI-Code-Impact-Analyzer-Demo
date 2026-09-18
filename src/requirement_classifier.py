def classify_requirement(text):

    if "safety" in text.lower():
        return "Safety"

    if "security" in text.lower():
        return "Security"

    return "General"