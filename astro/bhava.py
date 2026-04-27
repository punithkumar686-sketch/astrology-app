def build_bhava_chart(planets):
    houses = {f"{i}H": [] for i in range(1, 13)}

    i = 0
    for planet, data in planets.items():
        house = f"{(i % 12) + 1}H"
        houses[house].append(f"{planet} ({data['sign']})")
        i += 1

    return houses
