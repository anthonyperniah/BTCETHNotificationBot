from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import json


def read_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    creator = config['creator']
    id_bot = config['id_bot']
    return id_bot


def start(update, context):
    update.message.reply_text('hola anthony')


def main(id_bot):
    updater = Updater(token=id_bot, use_context=True)
    dp = updater.dispatcher
    # Add handler
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    id_bot = read_config()
    main(id_bot)
