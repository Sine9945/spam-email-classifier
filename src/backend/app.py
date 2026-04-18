from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('email', '')

    if "free" in text.lower() or "win" in text.lower() or "lottery" in text.lower():
        result = "Spam"
    else:
        result = "Not Spam"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)