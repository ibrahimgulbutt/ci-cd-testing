from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__, template_folder="../frontend")
CORS(app)

# API endpoint: Hello message
@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask backend!"})

# API endpoint: Add two numbers
@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})

# API endpoint: Reverse a string
@app.route("/api/reverse", methods=["POST"])
def reverse():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify({"resultt": text[::-1]})

# API endpoint: Get a random motivational quote
import random
QUOTES = [
    "Believe in yourself!",
    "You can do it!",
    "Never give up!",
    "Stay positive and strong!",
    "Success is a journey, not a destination."
]
@app.route("/api/quote")
def quote():
    return jsonify({"quote": random.choice(QUOTES)})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
