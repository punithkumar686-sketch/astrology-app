from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy kundli data (we will upgrade later to real ephemeris)
def generate_chart():
    houses = [
        "Asc", "2H", "3H", "4H",
        "5H", "6H", "7H", "8H",
        "9H", "10H", "11H", "12H"
    ]

    planets = [
        "Sun", "Moon", "Mars", "Mercury",
        "Jupiter", "Venus", "Saturn"
    ]

    chart = {}

    for i, house in enumerate(houses):
        chart[house] = planets[i % len(planets)]

    return chart


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/kundli")
def kundli():
    chart = generate_chart()
    return render_template("kundli.html", chart=chart)


@app.route("/chart")
def chart():
    chart = generate_chart()
    return render_template("chart.html", chart=chart)


@app.route("/match")
def match():
    return render_template("match.html")


@app.route("/dasha")
def dasha():
    return render_template("dasha.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
