import time

import requests
import telebot
import json
from telebot import types

bot = telebot.TeleBot('2051356841:AAEXX3HBQU8IJHsM4t3jSe4QgxbNyt3kP8g')
keyboard = [
    [types.InlineKeyboardButton('BTC (Bitcoin)', callback_data="BTC")],
    [types.InlineKeyboardButton('LTC (Litecoin)', callback_data="LTC")],
    [types.InlineKeyboardButton('ETH (Ethereum)', callback_data="ETH")],
]
menu_markup = types.InlineKeyboardMarkup(keyboard)


def getValue(cur):
    # https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker
    # https: // blockchain.info / ticker
    # https://developers.coinbase.com/api/v2?python#show-a-payment-method
    # https://api.coinbase.com/v2/exchange-rates?currency=ETH
    response = requests.get("https://api.coinbase.com/v2/prices/" + cur + "/buy")
    data = response.content
    dataJson = json.loads(data)
    price = dataJson["data"]["amount"]
    return price


@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "BTC":
        bot.send_message(call.message.chat.id, text=f"*1BTC =* *{getValue('BTC-USD')}*$", parse_mode='Markdown')
    if call.data == "LTC":
        bot.send_message(call.message.chat.id, text=f"*1LTC =* *{getValue('LTC-USD')}*$", parse_mode='Markdown')
    if call.data == "ETH":
        bot.send_message(call.message.chat.id, text=f"*1ETH =* *{getValue('ETH-USD')}*$", parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, 'Вітаю! Радий тебе бачити!')
    bot.send_message(message.chat.id, 'Я - чат-бот, знаю курси криптовалют.')
    bot.send_message(message.chat.id, 'Ось доступні команди, які ти можеш використовувати: '
                                      '\n/showCurrency - Показати доступні валюти та їх курс '
                                      '\n/convert - Конвертер валюти з долара у криптовалюту')


@bot.message_handler(commands=['showCurrency'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Choose currency", reply_markup=menu_markup)


@bot.message_handler(commands=['convert'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Це демо -версія бота для повного доступу до "
                                      "всіх функцій оплати дану послугу у "
                                      "розмірі 50 доларів")
    bot.send_message(509033294, "Заюзали функцію конвертора")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDG6RhbXbPdR5hZwZIdXl7ixv5NTK8-AACNQoAAipVGAJiqlHrnxhNcyEE")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDG6ZhbXet8dgshrqozx5jgrlUVQQlrgACAQAD2EMzEhQHRg4mxq7iIQQ")
    time.sleep(5)
    bot.send_message(message.chat.id, "Шутка ☺☺☺, даний розділ ще в розробці")


bot.polling()
