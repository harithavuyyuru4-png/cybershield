from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# words list
bad_words = ["kill", "fuck", "stupid", "idiot", "hate"]

# homepage
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CyberShield</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:100px;">
        <h1>CyberShield - Cyberbullying Detector</h1>
        <form action="/predict" method="post">
            <input type="text" name="message" placeholder="Enter message" style="padding:10px;width:300px;">
            <br><br>
            <button type="submit" style="padding:10px 20px;">Check Message</button>
        </form>
    </body>
    </html>
    """

# prediction
@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    if any(word in message.lower() for word in bad_words):
        return "<h2 style='color:red;text-align:center;margin-top:100px;'>Cyberbullying Detected</h2>"
    else:
        return "<h2 style='color:green;text-align:center;margin-top:100px;'>Not Cyberbullying</h2>"

# run server
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
