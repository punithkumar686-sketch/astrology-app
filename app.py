from flask import Flask, render_template, request
import swisseph as swe
import datetime
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 🔮 Get Rashi from longitude
def get_rashi(longitude):
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    return signs[int(longitude / 30)]

# 🌌 Calculate planetary positions
def calculate_chart(dob, time, place):
    date = datetime.datetime.strptime(dob + " " + time, "%d/%m/%Y %H:%M")

    jd = swe.julday(date.year, date.month, date.day, date.hour)

    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]

    sun_sign = get_rashi(sun)
    moon_sign = get_rashi(moon)

    return sun_sign, moon_sign

# 🤖 AI Prediction
def generate_prediction(name, dob, time, place, sun_sign):
    prompt = f"""
User: {name}
DOB: {dob}, Time: {time}, Place: {place}
Sun Sign: {sun_sign}

Give 5-year prediction:
Career, Wealth, Marriage
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)  # shows in Render logs
        return "⚠️ Prediction temporarily unavailable. Please try again later."
        
# 🏠 Route
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    sun_sign = ""
    moon_sign = ""

    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        time = request.form['time']
        place = request.form['place']

        sun_sign, moon_sign = calculate_chart(dob, time, place)

        prediction = generate_prediction(
            name, dob, time, place, sun_sign, moon_sign
        )

    return render_template("index.html",
                           prediction=prediction,
                           sun_sign=sun_sign,
                           moon_sign=moon_sign)

# 🚀 Run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
