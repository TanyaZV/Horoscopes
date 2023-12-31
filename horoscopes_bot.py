# ссылка: https://t.me/EverydayHoroscopesBot

import os
from background import keep_alive
import time
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b4
from datetime import datetime as dt

aries = 'Овен\n(21.03 - 19.04)'
taurus = 'Телец\n(20.04 - 20.05)'
gemini = 'Близнецы\n(21.05 - 21.06)'
cancer = 'Рак\n(22.06 - 22.07)'
leo = 'Лев\n(23.07 - 23.08)'
virgo = 'Дева\n(24.08 - 22.09)'
libra = 'Весы\n(23.09 - 23.10)'
scorpio = 'Скорпион\n(24.10 - 22.11)'
sagittarius = 'Стрелец\n(23.11 - 21.12)'
capricorn = 'Козерог\n(22.12 - 19.01)'
aquarius = 'Водолей\n(20.01 - 18.02)'
pisces = 'Рыбы\n(19.02 - 20.03)'

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    name_aries = types.KeyboardButton(aries)
    name_taurus = types.KeyboardButton(taurus)
    name_gemini = types.KeyboardButton(gemini)
    name_cancer = types.KeyboardButton(cancer)
    name_leo = types.KeyboardButton(leo)
    name_virgo = types.KeyboardButton(virgo)
    name_libra = types.KeyboardButton(libra)
    name_scorpio = types.KeyboardButton(scorpio)
    name_sagittarius = types.KeyboardButton(sagittarius)
    name_capricorn = types.KeyboardButton(capricorn)
    name_aquarius = types.KeyboardButton(aquarius)
    name_pisces = types.KeyboardButton(pisces)
    markup.add(name_aries, name_taurus, name_gemini, name_cancer, name_leo, name_virgo, name_libra, name_scorpio, name_sagittarius, name_capricorn, name_aquarius, name_pisces)
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>, выберете знак зодиака и немного подождите.', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def handler(message):
    def parser(url):
        r = requests.get(url)
        soup = b4(r.text, 'html.parser')
        ans = '\n'.join([i.text for i in (soup.find_all('div', class_='article__text'))]).split('\n')
        return ans

    URL = None
    if message.text == aries:
        URL = 'https://horo.mail.ru/prediction/aries/today/'
    elif message.text == taurus:
        URL = 'https://horo.mail.ru/prediction/taurus/today/'
    elif message.text == gemini:
        URL = 'https://horo.mail.ru/prediction/gemini/today/'
    elif message.text == cancer:
        URL = 'https://horo.mail.ru/prediction/cancer/today/'
    elif message.text == leo:
        URL = 'https://horo.mail.ru/prediction/leo/today/'
    elif message.text == virgo:
        URL = 'https://horo.mail.ru/prediction/virgo/today/'
    elif message.text == libra:
        URL = 'https://horo.mail.ru/prediction/libra/today/'
    elif message.text == scorpio:
        URL = 'https://horo.mail.ru/prediction/scorpio/today/'
    elif message.text == sagittarius:
        URL = 'https://horo.mail.ru/prediction/sagittarius/today/'
    elif message.text == capricorn:
        URL = 'https://horo.mail.ru/prediction/capricorn/today/'
    elif message.text == aquarius:
        URL = 'https://horo.mail.ru/prediction/aquarius/today/'
    elif message.text == pisces:
        URL = 'https://horo.mail.ru/prediction/pisces/today/'
    if URL != None:
        list_ans_1 = str(parser(URL)[0])
        list_ans_2 = str(parser(URL)[1])
        now_day = dt.now().day
        now_month = dt.now().month
        if now_day < 10:
          now_day = '0' + str(now_day)
        if now_month < 10:
          now_month = '0' + str(now_month)
        bot.send_message(message.chat.id, f'<b>Гороскоп на {now_day}.{now_month}:</b>\n\n{list_ans_1}\n\n{list_ans_2}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Простите, я не понимаю')

keep_alive()
bot.polling(non_stop=True, interval=0)
