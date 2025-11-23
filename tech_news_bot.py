import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Get bot token from environment variable
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Please set TELEGRAM_BOT_TOKEN in environment variables.")

# Delete existing webhook
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

delete_webhook()

# /start command — ONLY shows description and available commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Tech News Bot.\n\n"
        "You can use the following commands to get news:\n"
        "/news - Latest tech news\n"
        "/ai - AI news\n"
        "/entertainment - Entertainment news\n"
        "/sports - Sports news\n"
        "/business - Business news\n"
        "/health - Health news\n\n"
        "Just type any of the commands above to get started."
    )

# /news and other categories — shared handler
async def news_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category = update.message.text.lstrip("/").lower()

    # Ignore /start so it does nothing
    if category == "start":
        return

    # Placeholder for actual news logic
    await update.message.reply_text(f"Here is the latest {category.capitalize()} news (placeholder).")

# Build the bot
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news_category))
app.add_handler(CommandHandler("ai", news_category))
app.add_handler(CommandHandler("entertainment", news_category))
app.add_handler(CommandHandler("sports", news_category))
app.add_handler(CommandHandler("business", news_category))
app.add_handler(CommandHandler("health", news_category))

# Run the bot
if __name__ == "__main__":
    print("Bot is starting...")
    app.run_polling()
