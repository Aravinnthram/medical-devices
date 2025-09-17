# simple wrapper to expose the Flask `app` variable to Vercel
from app import app  # import the Flask app defined in app.py
# Vercel uses the `app` variable (WSGI) automatically