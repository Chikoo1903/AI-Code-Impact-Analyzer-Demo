def classify_requirement(text):

    if "safety" in text.lower():
        return "Safety"

    return "General"