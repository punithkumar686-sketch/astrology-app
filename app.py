from flask import Flask, render_template, request
import swisseph as swe
from datetime import datetime

app = Flask(__name__)

# Swiss Ephemeris setup
swe.set_ephe_path('.')

# Planets
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

# 🔮 REAL KUNDLI GENERATOR
def generate_kundli(dob, tob, place):
    dt = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")

    jd = swe.julday(
        dt.year, dt.month, dt.day,
        dt.hour + dt.minute / 60
    )

    chart = []

    for name, planet in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet)
        deg = pos[0]
        sign = get_sign(deg)

        chart.append({
            "planet": name,
            "degree": round(deg, 2),
            "sign": sign
        })

    return chart


# 🏠 Home Page
@app.route("/")
def home():
    return render_template("index.html")


# 🔮 Result Page
@app.route("/kundli", methods=["POST"])
def kundli():
    dob = request.form.get("dob")
    tob = request.form.get("tob")
    place = request.form.get("place")

    chart = generate_kundli(dob, tob, place)

    return render_template("result.html", chart=chart, place=place)


if __name__ == "__main__":
    app.run(debug=True)
