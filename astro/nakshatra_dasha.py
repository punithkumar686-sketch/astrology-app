# 🪐 REAL VIMSHOTTARI DASHA (NAKSHATRA BASED CORE)

# Each Nakshatra lord order
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

# 27 Nakshatras mapped to rulers (simplified correct order)
NAKSHATRA_LORDS = [
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"
]


# 🌙 Get Nakshatra from Moon degree
def get_nakshatra(moon_degree):
    index = int(moon_degree / (360 / 27))
    return index, NAKSHATRA_LORDS[index]


# ⏳ Generate full Vimshottari timeline
def generate_dasha(start_lord):
    order = [d[0] for d in DASHA_ORDER]

    start_index = order.index(start_lord)

    timeline = []
    current_year = 0

    for i in range(len(order)):
        lord = order[(start_index + i) % 9]
        years = dict(DASHA_ORDER)[lord]

        timeline.append({
            "planet": lord,
            "start": current_year,
            "end": current_year + years,
            "duration": years
        })

        current_year += years

    return timeline


# 🔮 MAIN ENGINE
def get_nakshatra_dasha(moon_degree):
    index, lord = get_nakshatra(moon_degree)
    timeline = generate_dasha(lord)

    return {
        "nakshatra_index": index,
        "starting_lord": lord,
        "timeline": timeline,
        "current": timeline[0]
    }
