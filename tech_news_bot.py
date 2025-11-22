from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Get your bot token from environment variable for security
TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable.")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your Tech News Bot. Send /news to get updates.")

# /news command
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Replace this with AI or news fetch logic
    await update.message.reply_text("Here is the latest tech news (placeholder).")

# Build the bot
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))

# Run the bot with polling
if __name__ == "__main__":
    print("Bot is starting...")
    app.run_polling()
