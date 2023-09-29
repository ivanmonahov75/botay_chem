import datetime
import os
import telebot
import telebot
from dotenv import load_dotenv
import yaml

with open('locales/all.yaml') as ym:
    templates = yaml.safe_load(ym)


def get_env(name):
    load_dotenv()
    return os.getenv(name)


def log(*args):
    print(datetime.datetime.now(), end=' ')
    for i in args:
        print(i, end=' ')
    with open('logs/all.log', 'a') as logs:
        for i in args:
            logs.write(i + ' ')
        logs.write('\n')


bot = telebot.TeleBot(get_env('TOKEN'))


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, templates['greeting'])
    log(message.from_user.username, message.text)


@bot.message_handler(commands=['get_element'])
def bot_element(message):
    bot.send_message(message.chat.id, message.text)
    log(message.from_user.username, message.text)
    # after that command user will choose anything (in separate message)


@bot.message_handler(commands=['get_theme'])
def bot_element(message):
    bot.send_message(message.chat.id, message.text)
    log(message.from_user.username, message.text)


bot.infinity_polling()
