# 🪐 Vimshottari Dasha Engine (Simplified Professional Version)

DASHA_ORDER = [
    ("Ketu", 7),
    ("Venus", 20),
    ("Sun", 6),
    ("Moon", 10),
    ("Mars", 7),
    ("Rahu", 18),
    ("Jupiter", 16),
    ("Saturn", 19),
    ("Mercury", 17)
]


def get_vimshottari_dasha():
    """
    Returns full Mahadasha timeline
    """
    timeline = []
    start_year = 0

    for planet, years in DASHA_ORDER:
        end_year = start_year + years

        timeline.append({
            "planet": planet,
            "start": start_year,
            "end": end_year,
            "duration": years
        })

        start_year = end_year

    return timeline


# 🌙 Simple interpretation engine (AI-style output layer)
def dasha_prediction():
    return {
        "current": "Moon Mahadasha",
        "interpretation": "Emotional growth, mental transformation, intuition increase.",
        "advice": "Focus on stability, avoid emotional decisions."
    }
