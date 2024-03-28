import logging
import os
from email import message

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Go to work')
async def villige(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'You live in villige Dmitrovichy')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()
    if 'hello' in message:
        reply_text = f'hello {update.effective_user.first_name} {update.effective_user.last_name}'
    elif 'goodbye' in message:
        if update.effective_user.last_name:
         reply_text = f'goodbye {update.effective_user.first_name} {update.effective_user.last_name}'
        else:
            reply_text = f'goodbye {update.effective_user.first_name}'
    else:
        reply_text = 'L dont understand you'
    await update.message.reply_text(reply_text)




app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("villige", villige))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
