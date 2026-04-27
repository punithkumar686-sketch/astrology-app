import swisseph as swe
from datetime import datetime

swe.set_ephe_path('.')

SIGNS = [
    "Aries","Taurus","Gemini","Cancer","Leo","Virgo",
    "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"
]

def get_sign(deg):
    return SIGNS[int(deg / 30)]


# 🌍 REAL LAGNA + PLANETS
def calculate_chart(dob, tob, lat=12.9716, lon=77.5946):
    dt = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")

    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60)

    # 🏠 REAL ASCENDANT (LAGNA)
    houses, ascmc = swe.houses(jd, lat, lon)
    lagna_deg = ascmc[0]
    lagna_sign = get_sign(lagna_deg)

    # 🪐 PLANETS
    planets = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN,
    }

    result = {}

    for name, p in planets.items():
        pos, _ = swe.calc_ut(jd, p)
        deg = pos[0]

        result[name] = {
            "degree": round(deg, 2),
            "sign": get_sign(deg)
        }

    return result, {
        "lagna_degree": round(lagna_deg, 2),
        "lagna_sign": lagna_sign
    }
