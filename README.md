# Text-Summarizer
A basic Text Summarizer application tool that uses Hugging Face's Transformers (BART model) and a Flask backend. You can input long text and receive a concise summary using NLP models.

---

## Features

- Input long-form text through a browser
- Backend summarization using sshleifer/distilbart-cnn-12-6 (smaller BART model)
- JSON-based API with Flask
- Deployment using WSGI server (e.g. Gunicorn)
- Frontend built with plain HTML + JavaScript

---

## Project Structure

Text_Summarizer/
- vercel-frontend/
   - assets/background.jgp #background image
   - index.html            #frontend UI
   - input.js              #javaScript for interacting with API
- app.py                  #main Flask app
- wsgi.py                 #WSGI entry point for deployment
- requirements.txt        #Dependencies
- README.md               #Project overview (this file)

---

## How it works

The input text getting from frontend is taken to backend though Flask API, where the text goes through the pretrained BART model for summarization (which is available publically in HuggingFace.co) and the output, i.e., the generated summary is printed in the frontend.

---

## Deployment

Frontend - Deployed through vercel.com
  Root directory: vercel-frontend

Backend - Built and deployed through Railway.com
  Environment Variable "HF_TOKEN" added with value of an API Token generated from HuggingFace.co
