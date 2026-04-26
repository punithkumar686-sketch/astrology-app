from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# 🔮 Simple Rashi logic
def get_rashi_from_date(dob):
    day, month, year = map(int, dob.split("-"))

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

# 🔥 Unique prediction engine (NO AI)
def generate_prediction(name, dob, time, place, sun_sign):
    year = int(dob.split("-")[0])
    seed = sum(ord(c) for c in name) + year
    random.seed(seed)

    career = random.choice([
        "Promotion or job upgrade",
        "Career shift to better role",
        "Business success",
        "Foreign opportunity",
        "Leadership growth"
    ])

    wealth = random.choice([
        "Strong savings growth",
        "Investment gains",
        "Property purchase",
        "Need financial discipline",
        "Sudden gains"
    ])

    marriage = random.choice([
        "Marriage within 2–3 years",
        "Delayed but stable marriage",
        "Love marriage chances",
        "Family-arranged marriage",
        "Focus on career first"
    ])

    return f"""
🔮 Astrology Report for {name}

☀ Sun Sign: {sun_sign}

━━━━━━━━━━━━━━━━━━━━━

📅 1–2 Years:
Career: {career}
Wealth: {wealth}

📅 3–4 Years:
Stable growth and strong financial position.

📅 5 Years:
Peak success and recognition.

💍 Marriage:
{marriage}

━━━━━━━━━━━━━━━━━━━━━
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    sun_sign = ""

    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        time = request.form['time']
        place = request.form['place']

        sun_sign = get_rashi_from_date(dob)
        prediction = generate_prediction(name, dob, time, place, sun_sign)

    return render_template("index.html",
                           prediction=prediction,
                           sun_sign=sun_sign)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
