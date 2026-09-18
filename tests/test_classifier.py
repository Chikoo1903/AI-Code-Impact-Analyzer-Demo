from src.requirement_classifier import classify_requirement

def test_classification():

    assert classify_requirement(
        "Safety requirements"
    ) == "Safety"