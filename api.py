from flask import Flask, request, jsonify
from google.generativeai import configure, GenerativeModel
import os

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
configure(api_key=GEMINI_API_KEY)
model = GenerativeModel('gemini-pro')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "CyberMasterAI API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)