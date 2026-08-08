def calculate_score(results):
    good = sum(1 for i in results if i["category"] == "Good")
    moderate = sum(1 for i in results if i["category"] == "Moderate")
    harmful = sum(1 for i in results if i["category"] == "Harmful")

    total = good + moderate + harmful

    if total == 0:
        score = 0
    else:
        score = max(0, min(10, round(((good * 1 + moderate * 0.5) / total) * 10, 1)))

    return {
        "score": score,
        "good": good,
        "moderate": moderate,
        "harmful": harmful
    }