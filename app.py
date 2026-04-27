from flask import Flask, render_template, request
from astro.charts import build_chart
from astro.dasha import get_dasha

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chart", methods=["POST"])
def chart():
    dob = request.form.get("dob")
    tob = request.form.get("tob")

    kundli = build_chart(dob, tob)

    return render_template("chart.html", kundli=kundli)


@app.route("/match")
def match():
    return render_template("match.html")


@app.route("/dasha")
def dasha():
    return render_template("dasha.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
