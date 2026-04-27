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


def calculate_planets(dob, tob):
    dt = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60)

    result = {}

    for name, planet in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet)
        deg = pos[0]

        result[name] = {
            "degree": round(deg, 2),
            "sign": get_sign(deg)
        }

    return result
