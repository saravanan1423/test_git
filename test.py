from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello, Flask! 🚀"

# Simple API (GET)
@app.route("/api/hello", methods=["GET"])
def hello_api():
    return jsonify({
        "message": "Hello from Flask API"
    })

# Simple API (POST)
@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)

    return jsonify({
        "sum": a + b
    })

if __name__ == "__main__":
    app.run(debug=True)
