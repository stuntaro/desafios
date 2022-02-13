import json
import requests
import logging

from os import getenv

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

log = logging.getLogger(__name__)

token = getenv("TELEGRAM_TOKEN")
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def nada_pra_fazer(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.to_dict()["text"]
    categories = message.split(" ")[-1]
    url = "http://crawlers_api:8080/redditer"
    params = {"categories": categories}
    response = requests.get(url, params=params)
    text = json.loads(response.content)
    context.bot.send_message(chat_id=chat_id,
                             text=json.dumps(text, indent=4, sort_keys=True))


if __name__ == '__main__':
    nada_pra_fazer_hander = CommandHandler("NadaPraFazer", nada_pra_fazer,
                                           run_async=True)
    dispatcher.add_handler(nada_pra_fazer_hander)
    updater.start_polling()
