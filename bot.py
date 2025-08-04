from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "6488229790:AAF4z5GLHrD8j5pGulTICI09suUlHZvaldA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    tracking_link = f"https://telegram-location-bot-9in0.onrender.com/track?id={chat_id}"
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"👋 Welcome! Here is your unique tracking link:\n{tracking_link}\n\nSend this to someone. When they open it, you'll get their location here!"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
