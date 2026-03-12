from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple cyberbullying words list
bad_words = ["kill", "fuck", "stupid", "idiot", "hate", "die"]

@app.route("/")
def home():
    return """
    <h2>CyberShield - Cyberbullying Detection</h2>
    <form action="/predict" method="post">
        <input type="text" name="message" placeholder="Enter message here">
        <button type="submit">Check</button>
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form.get("message")

    if any(word in message.lower() for word in bad_words):
        result = "Cyberbullying Detected"
    else:
        result = "Not Cyberbullying"

    return f"<h3>Result: {result}</h3><br><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run()