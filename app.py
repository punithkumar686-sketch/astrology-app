def generate_kundli():
    year, month, day = 1994, 3, 27
    hour, minute = 12, 32

    jd = swe.julday(year, month, day, hour + minute / 60)

    planets_data = {}

    for name, planet in PLANETS.items():
        result = swe.calc_ut(jd, planet)

        deg = result[0][0] if isinstance(result[0], (list, tuple)) else result[0]

        sign = get_sign(deg)

        planets_data[name] = {
            "degree": round(deg, 2),
            "sign": sign
        }

    house_chart = {h: [] for h in HOUSES}

    i = 0
    for planet, data in planets_data.items():
        house = HOUSES[i % 12]
        house_chart[house].append(f"{planet} ({data['sign']})")
        i += 2

    return house_chart
