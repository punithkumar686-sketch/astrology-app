def compatibility_score():
    import random

    score = random.randint(18, 34)  # placeholder AI logic

    if score > 30:
        status = "Excellent Match 💖"
    elif score > 24:
        status = "Good Match 👍"
    else:
        status = "Average Match ⚠️"

    return score, status
