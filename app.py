from flask import Flask, render_template, request

app = Flask(__name__)

def generate_prediction(dob, time, place):
    # SIMPLE VERSION (you can upgrade later)
    return f"""
    🔮 Astrology Report

    Career:
    Next 1-2 years: Growth with challenges.
    3-5 years: Strong success and financial stability.

    Wealth:
    Gradual increase. Major gains around year 3.

    Marriage:
    Likely between year 2-4 depending on decisions.
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

if __name__ == '__main__':
    app.run(debug=True)
