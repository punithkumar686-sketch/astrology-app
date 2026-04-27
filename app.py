from flask import Flask, render_template, request
from astro.charts import build_kundli
from astro.match import compatibility_score
from astro.dasha import get_dasha

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chart", methods=["POST"])
def chart():
    dob = request.form.get("dob")
    tob = request.form.get("tob")

    kundli, lagna = build_kundli(dob, tob)

    return render_template("chart.html", kundli=kundli, lagna=lagna)


@app.route("/match")
def match():
    score, status = compatibility_score()
    return render_template("match.html", score=score, status=status)


@app.route("/dasha")
def dasha():
    data = get_dasha()
    return render_template("dasha.html", dasha=data)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
