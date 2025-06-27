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
- app.py  #Main Flask app
- wsgi.py  #WSGI entry point for deployment
- home.html  #Frontend UI
- input.js  #JavaScript for interacting with API
- packages.txt #Dependencies
- README.md  #Project overview (this file)
- .gitignore #Files ignored in version control
