from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    text = data['text'].lower()

    abusive_words = [
        "stupid",
        "idiot",
        "ugly",
        "hate",
        "fool",
        "fuck",
        "kill",
        "bastard",
        "moron",
        "dumb",
        "loser",
        "shut up"
    ]

    result = "Not Cyberbullying"

    for word in abusive_words:
        if word in text:
            result = "Cyberbullying"
            break

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)