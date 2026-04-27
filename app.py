from flask import Flask, render_template, request
from astro.charts import build_kundli

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chart", methods=["POST"])
def chart():
    dob = request.form.get("dob")
    tob = request.form.get("tob")

    planets, lagna = build_kundli(dob, tob)

    return render_template("chart.html", planets=planets, lagna=lagna)


@app.route("/match")
def match():
    return render_template("match.html")


@app.route("/dasha")
def dasha():
    return render_template("dasha.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
