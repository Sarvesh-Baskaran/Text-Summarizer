from flask import Flask, request, jsonify
#from transformers import BartForConditionalGeneration, BartTokenizer
import requests
#import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enables CORS for frontend to access API

# Load model and tokenizer (you can cache this to avoid reloading every time)
api_token = os.getenv("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")
#endpoint for model
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {api_token}"}

#model_name = "sshleifer/distilbart-cnn-12-6"
#tokenizer = BartTokenizer.from_pretrained(model_name)
#model = BartForConditionalGeneration.from_pretrained(model_name)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    if response.status_code != 200:
        return jsonify({
            "error": "Failed to summarize",
            "details": response.text
        }), 500

    try:
        summary_text = response.json()[0]['summary_text']
        return jsonify({"summary": summary_text})
    except Exception as e:
        return jsonify({
            "error": "Unexpected response format",
            "details": str(e)
        }), 500
