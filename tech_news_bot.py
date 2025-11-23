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

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Tech News Bot.\nSend /news to get the latest updates."
    )

# /news command
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Placeholder: Replace with your n8n workflow call or AI agent
    await update.message.reply_text("Here is the latest tech news (placeholder).")

# Delete any webhook to allow polling
delete_webhook()

# Build the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))
# /ai command
async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the latest AI news (placeholder).")

# /entertainment command
async def entertainment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the latest Entertainment news (placeholder).")

# /sports command
async def sports(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the latest Sports news (placeholder).")

# /business command
async def business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the latest Business news (placeholder).")

# /health command
async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the latest Health news (placeholder).")

# Add handlers for the new commands
app.add_handler(CommandHandler("ai", ai))
app.add_handler(CommandHandler("entertainment", entertainment))
app.add_handler(CommandHandler("sports", sports))
app.add_handler(CommandHandler("business", business))
app.add_handler(CommandHandler("health", health))

# Run the bot with polling (Railway uses a dynamic PORT but polling ignores it)
if __name__ == "__main__":
    print("Bot is starting...")
    app.run_polling()
