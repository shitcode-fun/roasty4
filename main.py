import os
import logging
import traceback
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Frontend:
    def __init__(self, token: str):
        self.application = ApplicationBuilder().token(token).build()
        self.application.add_handler(CommandHandler('start', self.start))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello! I'm your new Telegram bot.")

    def run(self):
        """Start the bot by running polling with pending updates dropped."""
        self.application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    bot_token = os.getenv('TELEGRAM_TOKEN')
    try:
        bot = Frontend(bot_token)
        bot.run()
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        logger.error(traceback_str) 