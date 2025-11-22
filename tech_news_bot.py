# bot.py

import os
import asyncio
import logging
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------------------
# 1. Setup logging
# ---------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ---------------------------
# 2. Asyncio patch for Railway / Linux environments
# ---------------------------
nest_asyncio.apply()

# ---------------------------
# 3. Get bot token from environment
# ---------------------------
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Bot token not set! Add TOKEN in Railway environment variables.")

# ---------------------------
# 4. Command handlers
# ---------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to /start"""
    await update.message.reply_text(
        "Hello! I am your Tech News Bot. Use /quote to get the latest tech summary."
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to /quote with a placeholder tech news summary"""
    tech_news_samples = [
        "AI startup raises $50M in funding.",
        "New Python version released with performance improvements.",
        "Quantum computing breakthrough announced in Europe.",
        "Tech giants announce new privacy standards.",
        "OpenAI releases updated GPT model for developers."
    ]
    import random
    summary = random.choice(tech_news_samples)
    await update.message.reply_text(f"Tech News Summary: {summary}")

# ---------------------------
# 5. Build application
# ---------------------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))

# ---------------------------
# 6. Run the bot
# ---------------------------
asyncio.get_event_loop().create_task(app.run_polling())

# Keep script running
print("Bot is running...")
asyncio.get_event_loop().run_forever()
