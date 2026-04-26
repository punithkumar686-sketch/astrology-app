from flask import Flask, render_template, request
import os

app = Flask(__name__)

def generate_prediction(dob, time, place):
    return f"""
🔮 Astrology Report

DOB: {dob}
Time: {time}
Place: {place}

Career:
Strong growth in next 2–3 years.

Wealth:
Gradual increase, peak around year 3.

Marriage:
Likely between 2–4 years window.
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        dob = request.form['dob']
        time = request.form['time']
        place = request.form['place']
        prediction = generate_prediction(dob, time, place)

    return render_template('index.html', prediction=prediction)

# ✅ ONLY ONE RUN BLOCK (IMPORTANT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses this
    app.run(host="0.0.0.0", port=port)
