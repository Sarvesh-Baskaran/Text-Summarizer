from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enables CORS for frontend to access API

#load model and tokenizer (you can cache this to avoid reloading every time)
#HF_TOKEN mentioned as a environment variable in railway.com
api_token = os.getenv("HF_TOKEN")
#endpoint for model
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {api_token}"}

#summarize function to call in input.js
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    #getting response from api_token in huggingface
    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    if response.status_code != 200:
        print("HuggingFace error: ", response.status_code, response.text)
        return jsonify({
            "error": "Failed to summarize",
            "details": response.text
        }), 500

    try:
        summary_text = response.json()[0]['summary_text']
        return jsonify({"summary": summary_text})
    except Exception as e:
        print("Parsing error: ",e, response.text)
        return jsonify({
            "error": "Unexpected response format",
            "details": str(e)
        }), 500
