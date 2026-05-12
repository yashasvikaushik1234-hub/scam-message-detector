from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def analyze_job_message(message):
    message = message.lower()
    score = 0
    reasons = []

    if "earn" in message:
        score += 10
        reasons.append("Unrealistic earnings")

    if "no interview" in message:
        score += 20
        reasons.append("No interview required")

    if "work from home" in message:
        score += 15
        reasons.append("Work from home offer")

    if "limited seats" in message:
        score += 10
        reasons.append("Urgency tactic")

    return {
        "score": score,
        "reasons": reasons,
        "scam": score > 20
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data["message"]
    result = analyze_job_message(message)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)