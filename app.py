from flask import Flask, render_template, request
import joblib

app = Flask(__name__)   # 👈 THIS LINE IS MUST

model = joblib.load("smart_invest_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        change = float(request.form["change"])
        volume = float(request.form["volume"])
        prediction = model.predict([[change, volume]])
        result = prediction[0]

    return render_template("index.html", result=result)

# optional for local run
if __name__ == "__main__":
    app.run(debug=True)
