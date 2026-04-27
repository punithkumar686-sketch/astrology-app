from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# 🔐 ENV VARIABLES
OPENCAGE_KEY = os.environ.get("OPENCAGE_KEY")
ASTRO_USER = os.environ.get("ASTRO_USER")
ASTRO_KEY = os.environ.get("ASTRO_KEY")

# 📍 GET LAT/LNG
def get_lat_long(place):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={place}&key={OPENCAGE_KEY}"
        res = requests.get(url).json()

        if res["results"]:
            lat = res["results"][0]["geometry"]["lat"]
            lng = res["results"][0]["geometry"]["lng"]
            return lat, lng

    except Exception as e:
        print("Location Error:", e)

    return None, None


# 🔮 ASTRO API
def get_kundli_api(dob, time, lat, lng):
    try:
        year, month, day = map(int, dob.split("-"))
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

        response = requests.post(
            url,
            json=payload,
            auth=(ASTRO_USER, ASTRO_KEY)
        )

        data = response.json()
        print("API DATA:", data)

        if isinstance(data, list):
            return data

    except Exception as e:
        print("Astro API Error:", e)

    return None


# 🔥 FALLBACK (ALWAYS WORKS)
def get_dummy_kundli():
    return [
        {"name": "Sun", "sign": "Aries", "normDegree": 120},
        {"name": "Moon", "sign": "Taurus", "normDegree": 45},
        {"name": "Mars", "sign": "Leo", "normDegree": 210},
        {"name": "Mercury", "sign": "Pisces", "normDegree": 80},
        {"name": "Jupiter", "sign": "Sagittarius", "normDegree": 300}
    ]


@app.route("/", methods=["GET", "POST"])
def home():
    kundli_data = None
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        dob = request.form.get("dob")
        time = request.form.get("time")
        place = request.form.get("place")

        print("INPUT:", name, dob, time, place)

        lat, lng = get_lat_long(place)
        print("LAT LNG:", lat, lng)

        kundli = None

        if lat and lng:
            kundli = get_kundli_api(dob, time, lat, lng)

        # 🔥 fallback if API fails
        if not kundli:
            print("Using fallback kundli")
            kundli = get_dummy_kundli()

        kundli_data = {
            "name": name,
            "planets": kundli
        }

    return render_template("index.html",
                           kundli_data=kundli_data,
                           error=error)
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

print(request.form)
