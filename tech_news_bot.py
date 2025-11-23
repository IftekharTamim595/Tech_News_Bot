import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Please set TELEGRAM_BOT_TOKEN in environment variables.")

# Delete webhook
def delete_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    try:
        r = requests.get(url)
        print("Webhook status:", r.text)
    except Exception as e:
        print("Error deleting webhook:", e)

delete_webhook()

# /start command – ONLY description
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Tech News Bot.\n\n"
        "Available commands:\n"
        "/news - Tech news\n"
        "/ai - AI news\n"
        "/entertainment - Entertainment news\n"
        "/sports - Sports news\n"
        "/business - Business news\n"
        "/health - Health news\n\n"
        "Choose a category to get updates."
    )

# This function will forward allowed commands to n8n
async def forward_to_n8n(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    # List of allowed commands
    valid_commands = [
        "/news", "/ai", "/entertainment",
        "/sports", "/business", "/health"
    ]

    # Ignore /start safely
    if user_text == "/start":
        return  # DO NOTHING. No forwarding.

    if user_text in valid_commands:
        # FORWARD TO N8N WORKFLOW
        # Replace with your actual n8n webhook URL
        n8n_webhook = os.environ.get("N8N_WEBHOOK_URL")

        if n8n_webhook:
            requests.post(n8n_webhook, json={"message": user_text})

        return

# Build bot
app = ApplicationBuilder().token(TOKEN).build()

# Command handlers
app.add_handler(CommandHandler("start", start))

# Message handler for forwarding to n8n
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_n8n))
app.add_handler(MessageHandler(filters.COMMAND, forward_to_n8n))

# Run bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
