import os
import telegram
from telegram.ext import Updater, CommandHandler

# Telegram bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Tumhara Render link:
RENDER_DOMAIN = "https://rudelegalinternet.onrender.com"

# Start command handler
def start(update, context):
    user_id = update.message.chat_id
    track_link = f"{RENDER_DOMAIN}/track?id={user_id}"
    
    message = (
        "🔍 Hello! Click the link below to share your location:\n\n"
        f"{track_link}\n\n"
        "📍 Allow location access in browser when prompted."
    )
    
    context.bot.send_message(chat_id=user_id, text=message)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
