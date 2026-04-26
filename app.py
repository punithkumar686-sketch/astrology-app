from flask import Flask, render_template, request, send_file
import os
from openai import OpenAI
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

# 🔑 OpenAI setup
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 🔮 AI Prediction
def generate_prediction(name, dob, time, place):
    prompt = f"""
You are a highly skilled Vedic astrologer.

Give a detailed structured 5-year prediction:

1 Year, 2 Year, 3 Year, 4 Year, 5 Year

Focus on:
- Career
- Wealth
- Marriage

User:
Name: {name}
DOB: {dob}
Time: {time}
Place: {place}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# 📄 PDF Generator
def create_pdf(text):
    file_path = "report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []
    for line in text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))

    doc.build(content)
    return file_path


# 🏠 Main Route
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""

    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        time = request.form.get('time')
        place = request.form.get('place')

        prediction = generate_prediction(name, dob, time, place)

        # Save to session-like variable
        with open("last_report.txt", "w") as f:
            f.write(prediction)

    return render_template('index.html', prediction=prediction)


# 📥 Download PDF
@app.route('/download')
def download():
    if os.path.exists("last_report.txt"):
        with open("last_report.txt", "r") as f:
            text = f.read()
    else:
        text = "No report generated yet."

    pdf = create_pdf(text)
    return send_file(pdf, as_attachment=True)


# 🚀 Run (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
