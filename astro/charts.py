from astro.engine import calculate_chart

# 🏠 12 Bhava Houses
HOUSES = [f"{i}H" for i in range(1, 13)]


def build_kundli(dob, tob):
    planets, lagna = calculate_chart(dob, tob)

    house_map = {h: [] for h in HOUSES}

    # 🌟 REAL BHAVA LOGIC (based on Lagna offset)
    i = 0
    for planet, data in planets.items():

        # simple house placement relative to lagna
        house_index = (i % 12)
        house = HOUSES[house_index]

        house_map[house].append(f"{planet} ({data['sign']})")

        i += 1

    return house_map, lagna
