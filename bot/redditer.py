import logging

from os import getenv

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater


log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)

log = logging.getLogger(__name__)

token = getenv("TELEGRAM_TOKEN")
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def nada_pra_fazer(update: Update, context: CallbackContext) -> None:
    text = '<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.'
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=text)


def start(update: Update, context: CallbackContext) -> None:
    text = "I'm a bot, please talk to me!"
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    nada_pra_fazer_hander = CommandHandler("NadaPraFazer", nada_pra_fazer)
    dispatcher.add_handler(nada_pra_fazer_hander)
    updater.start_polling()
