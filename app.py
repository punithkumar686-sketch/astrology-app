from flask import Flask, render_template, request

app = Flask(__name__)

# 🔮 Dummy Kundli Generator (replace with real logic later)
def generate_kundli(dob, time, place):
    return f"""
    Kundli Generated Successfully!

    Date of Birth: {dob}
    Time of Birth: {time}
    Place: {place}

    🔥 Prediction: Strong growth and opportunities ahead.
    """

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


@app.route("/kundli", methods=["GET", "POST"])
def kundli():
    if request.method == "POST":

        # ✅ Debug (check terminal)
        print("FORM DATA:", request.form)

        dob = request.form.get("date_of_birth")
        time = request.form.get("time_of_birth")
        place = request.form.get("place")

        # Generate kundli result
        result = generate_kundli(dob, time, place)

        print("RESULT:", result)

        return render_template("result.html", result=result)

    # if user opens route directly
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
