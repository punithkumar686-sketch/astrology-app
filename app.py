from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 🔮 Prediction Function
def generate_prediction(name, dob, time, place):
    return f"""
🔮 Astrology Report for {name}

Birth Details:
Date: {dob}
Time: {time}
Place: {place}

━━━━━━━━━━━━━━━━━━━━━

📅 1-Year Forecast:
Career: Steady progress with new opportunities.
Wealth: Stable income, avoid risky investments.
Marriage: Possible developments in relationships.

━━━━━━━━━━━━━━━━━━━━━

📅 2-Year Forecast:
Career: Growth phase begins, chances of promotion/job switch.
Wealth: Increase in earnings.
Marriage: Strong possibility of commitment.

━━━━━━━━━━━━━━━━━━━━━

📅 3-Year Forecast:
Career: Major breakthrough or business success.
Wealth: Peak earning phase.
Marriage: Highly favorable for marriage.

━━━━━━━━━━━━━━━━━━━━━

📅 4-Year Forecast:
Career: Stability and leadership role.
Wealth: Savings and asset building.
Marriage: Harmonious family life.

━━━━━━━━━━━━━━━━━━━━━

📅 5-Year Forecast:
Career: Long-term success and recognition.
Wealth: Strong financial stability.
Marriage: Settled and supportive partnership.

━━━━━━━━━━━━━━━━━━━━━

✨ Overall Guidance:
Focus on consistent effort, avoid impulsive decisions, and build long-term assets.
"""

# 🏠 Home Route
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""

    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        time = request.form.get('time')
        place = request.form.get('place')

        prediction = generate_prediction(name, dob, time, place)

    return render_template('index.html', prediction=prediction)

# 🚀 Run App (Local + Render Compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
