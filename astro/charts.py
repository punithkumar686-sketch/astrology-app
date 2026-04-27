from astro.engine import calculate_chart

HOUSES = [f"{i}H" for i in range(1, 13)]

def build_kundli(dob, tob):
    planets = calculate_chart(dob, tob)

    house_map = {h: [] for h in HOUSES}

    i = 0
    for planet, data in planets.items():
        house = HOUSES[i % 12]
        house_map[house].append(f"{planet} ({data['sign']})")
        i += 1   # FIXED (was i += 2)

    lagna = planets.get("Lagna", None)  # safe fallback

    return house_map, lagna
