from flask import Flask, render_template, request
import os
import random
import requests

app = Flask(__name__)

# 🔮 Get Zodiac Sign
def get_rashi_from_date(dob):
    year, month, day = map(int, dob.split("-"))

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"
    else:
        return "pisces"

# 🔥 FREE API + PERSONALIZATION
def generate_prediction(name, dob, time, place, sun_sign):
    try:
        # Call Aztro API
        url = f"https://aztro.sameerkumar.website/?sign={sun_sign}&day=today"
        response = requests.post(url)
        data = response.json()

        # Personalization using seed
        seed = sum(ord(c) for c in name)
        random.seed(seed)

        career_addon = random.choice([
            "A new opportunity may change your path.",
            "Your leadership skills will be tested.",
            "A job switch may bring growth.",
            "You may explore business ideas."
        ])

        wealth_addon = random.choice([
            "Avoid risky investments.",
            "Savings will improve gradually.",
            "Unexpected gains possible.",
            "Focus on long-term investments."
        ])

        marriage_addon = random.choice([
            "Marriage prospects improve soon.",
            "Take time before commitment.",
            "Strong emotional connection likely.",
            "Family may influence decisions."
        ])

        return f"""
🔮 Astrology Report for {name}

📍 Place: {place}
☀ Sun Sign: {sun_sign.capitalize()}

━━━━━━━━━━━━━━━━━━━━━

🌟 Today's Horoscope:
{data.get('description', 'No data available')}

💼 Career:
{career_addon}

💰 Wealth:
{wealth_addon}

💍 Marriage:
{marriage_addon}

━━━━━━━━━━━━━━━━━━━━━

✨ Tip:
{data.get('advice', 'Stay positive and focused.')}
"""

    except Exception as e:
        print("ERROR:", e)

        # Fallback (no API)
        return f"""
⚠️ Could not fetch live horoscope.

🔮 Basic Prediction for {name}

☀ Sun Sign: {sun_sign.capitalize()}

Career: Growth through consistency  
Wealth: Stable with planning  
Marriage: Positive but requires patience  
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

    return render_template(
        "index.html",
        prediction=prediction,
        sun_sign=sun_sign.capitalize() if sun_sign else ""
    )

# 🚀 Render Deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
