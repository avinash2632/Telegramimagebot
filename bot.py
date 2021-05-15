import logging
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_url():
    url = "https://random.dog/12a9bb92-3c41-4f40-b37e-de275df7a292.JPG"
    return url



def start(update, context):

    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    context. bot.send_photo(chat_id, photo=url)
    """Send a message when the command /help is issued."""



def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    update.send_photo(chat_id=message.message_id, photo='https://telegram.org/img/t_logo.png')
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)




updater = Updater("1793354007:AAEpGtK7CtZcVUeOVfvelWxn588EKp3Ow6g", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

dp.add_handler(CommandHandler("help", help))
    # on noncommand i.e message - echo the message on Telegram
dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
dp.add_error_handler(error)

    # Start the Bot
updater.start_polling()

updater.idle()


