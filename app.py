from flask import Flask, render_template, request
import swisseph as swe
from datetime import datetime

app = Flask(__name__)

# Set ephemeris path (important)
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

def generate_kundli(dob, tob):
    dt = datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")

    jd = swe.julday(
        dt.year, dt.month, dt.day,
        dt.hour + dt.minute / 60.0
    )

    result = []

    for name, planet in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet)
        deg = pos[0]
        sign = get_sign(deg)

        result.append(f"{name}: {deg:.2f}° → {sign}")

    return "\n".join(result)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/kundli", methods=["POST"])
def kundli():
    dob = request.form.get("date_of_birth")
    tob = request.form.get("time_of_birth")
    place = request.form.get("place")

    chart = generate_kundli(dob, tob)

    return render_template("result.html", result=chart, place=place)


if __name__ == "__main__":
    app.run(debug=True)
