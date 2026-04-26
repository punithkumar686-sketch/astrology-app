from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)



# 🔑 API KEYS
OPENCAGE_KEY = "YOUR_OPENCAGE_KEY"
ASTRO_USER = "YOUR_ASTROLOGY_API_USER"
ASTRO_KEY = "YOUR_ASTROLOGY_API_KEY"

# 📍 Get Lat Long
def get_lat_long(place):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={place}&key={OPENCAGE_KEY}"
    res = requests.get(url).json()

    if res["results"]:
        lat = res["results"][0]["geometry"]["lat"]
        lng = res["results"][0]["geometry"]["lng"]
        return lat, lng
    return None, None

# 🔮 Get Kundli Data
def get_kundli(dob, time, lat, lng):
    day, month, year = map(int, dob.split("-"))
    hour, minute = map(int, time.split(":"))

    url = "https://json.astrologyapi.com/v1/planets"

    payload = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": minute,
        "lat": lat,
        "lon": lng,
        "tzone": 5.5
    }

    response = requests.post(url, json=payload, auth=(ASTRO_USER, ASTRO_KEY))

    return response.json()

@app.route("/", methods=["GET", "POST"])
def home():
    data = None

    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        time = request.form["time"]
        place = request.form["place"]

        lat, lng = get_lat_long(place)

        if lat and lng:
            kundli = get_kundli(dob, time, lat, lng)
            data = {
                "name": name,
                "kundli": kundli
            }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
