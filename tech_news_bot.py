from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import nest_asyncio

nest_asyncio.apply()

TOKEN = "8341638548:AAEG2YxPKgrV46X5m7jRDwKu7W-PC9LUvR0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your tech news bot.")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is your tech news summary!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))

asyncio.get_event_loop().create_task(app.run_polling())
