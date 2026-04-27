import swisseph as swe
from datetime import datetime

swe.set_ephe_path('.')

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
}

SIGNS = [
    "Aries","Taurus","Gemini","Cancer","Leo","Virgo",
    "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"
]


def get_sign(deg):
    return SIGNS[int(deg / 30)]


# 🌟 REAL LAGNA CALCULATION
def calculate_lagna(jd):
    houses = swe.houses(jd, 28.6139, 77.2090)[0]  # default India coords
    lagna = houses[0]
    return get_sign(lagna)


def calculate_chart(dob, tob):
    dt = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60)

    chart = {}

    for name, planet in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet)
        deg = pos[0]

        chart[name] = {
            "degree": round(deg, 2),
            "sign": get_sign(deg)
        }

    lagna = calculate_lagna(jd)

    return chart, lagna
