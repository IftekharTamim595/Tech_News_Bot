import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Get bot token from environment variable
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Please set TELEGRAM_BOT_TOKEN in environment variables.")

# Optional: Get PORT from Railway
PORT = int(os.environ.get("PORT", 8443))

# Function to remove existing webhook (avoids polling conflict)
def delete_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print("Existing webhook deleted:", r.json())
        else:
            print("Failed to delete webhook:", r.text)
    except Exception as e:
        print("Error deleting webhook:", e)

# /start command — description only, does nothing else
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Tech News Bot.\n"
        "Use the following commands to get news:\n"
        "/news - Latest tech news\n"
        "/ai - AI news\n"
        "/entertainment - Entertainment news\n"
        "/sports - Sports news\n"
        "/business - Business news\n"
        "/health - Health news"
    )

# Placeholder news function for all news commands
async def send_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category = update.message.text.lstrip("/").lower()
    await update.message.reply_text(f"Here is the latest {category} news (placeholder).")

# Delete any webhook to allow polling
delete_webhook()

# Build the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", send_news))
app.add_handler(CommandHandler("ai", send_news))
app.add_handler(CommandHandler("entertainment", send_news))
app.add_handler(CommandHandler("sports", send_news))
app.add_handler(CommandHandler("business", send_news))
app.add_handler(CommandHandler("health", send_news))

# Run the bot with polling
if __name__ == "__main__":
    print("Bot is starting...")
    app.run_polling()
