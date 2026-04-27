from astro.engine import calculate_planets

HOUSES = [f"{i}H" for i in range(1, 13)]

def build_chart(dob, tob):
    planets = calculate_planets(dob, tob)

    chart = {h: [] for h in HOUSES}

    i = 0
    for name, data in planets.items():
        house = HOUSES[i % 12]
        chart[house].append(f"{name} ({data['sign']})")
        i += 2

    return chart
