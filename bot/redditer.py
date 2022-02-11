import json
import logging

from os import getenv

from telegram import ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler, Updater

from crawlers.reddit import RedditCrawler


log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

log = logging.getLogger(__name__)

token = getenv("TELEGRAM_TOKEN")
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def nada_pra_fazer(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    log.info(update.message.to_dict())
    message = update.message.to_dict()["text"]
    categories = message.split(" ")[-1].split(";")
    crawler = RedditCrawler(categories, 5000)
    text = json.dumps(crawler.content(), indent=4, sort_keys=True)
    context.bot.send_message(chat_id=chat_id,
                             text=text)


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
