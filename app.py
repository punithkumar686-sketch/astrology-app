from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# 🔐 ENV VARIABLES (SET IN RENDER)
OPENCAGE_KEY = os.environ.get("OPENCAGE_KEY")
ASTRO_USER = os.environ.get("ASTRO_USER")
ASTRO_KEY = os.environ.get("ASTRO_KEY")

# 📍 GET LATITUDE & LONGITUDE FROM PLACE
def get_lat_long(place):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={place}&key={OPENCAGE_KEY}"
        response = requests.get(url).json()

        if response["results"]:
            lat = response["results"][0]["geometry"]["lat"]
            lng = response["results"][0]["geometry"]["lng"]
            return lat, lng

        return None, None

    except Exception as e:
        print("OpenCage Error:", e)
        return None, None


# 🔮 GET KUNDLI (PLANETS)
def get_kundli(dob, time, lat, lng):
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

        print("KUNDLI DATA:", data)  # debug

        return data

    except Exception as e:
        print("Astrology API Error:", e)
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    kundli_data = None
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        dob = request.form.get("dob")
        time = request.form.get("time")
        place = request.form.get("place")

        # Step 1: Get location
        lat, lng = get_lat_long(place)

        if not lat or not lng:
            error = "❌ Could not fetch location. Try another city."
        else:
            # Step 2: Get kundli
            kundli = get_kundli(dob, time, lat, lng)

            if not kundli or isinstance(kundli, dict) and kundli.get("error"):
                error = "⚠️ Kundli API failed (check API keys or trial limit)."
            else:
                kundli_data = {
                    "name": name,
                    "place": place,
                    "dob": dob,
                    "time": time,
                    "planets": kundli
                }

    return render_template(
        "index.html",
        kundli_data=kundli_data,
        error=error
    )


# 🚀 RUN SERVER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
