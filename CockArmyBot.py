#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import telebot
from telebot import types
token = '292704887:AAFq9AMtsJjvTWp5gfdVRiDxieEe6-kChTE'

bot = telebot.TeleBot(token)

def make_unit(unit):
    res=''
    for i in range(0,unit):
        res+='🐔'
    return res


@bot.inline_handler(lambda query: len(query.query) >= 0)
def query_text(query):
    results = []
    petuch = types.InlineQueryResultArticle(
        id="1",
		title="Разведчик 🐔",
        input_message_content=types.InputTextMessageContent(message_text="🐔")
    )
    group = types.InlineQueryResultArticle(
        id="2",
		title="Группа 🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(10))
    )
    vzvod = types.InlineQueryResultArticle(
        id="3",
		title="Взвод 🐔🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(45))
    )
    rota = types.InlineQueryResultArticle(
        id="4",
		title="Рота 🐔🐔🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(120))
    )
    batalion = types.InlineQueryResultArticle(
        id="5",
		title="Батальон 🐔🐔🐔🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(720))
    )
    polk = types.InlineQueryResultArticle(
        id="6",
		title="Полк 🐔🐔🐔🐔🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(990))
    )
    brigada = types.InlineQueryResultArticle(
        id="7",
		title="Бригада 🐔🐔🐔🐔🐔🐔🐔",
        input_message_content=types.InputTextMessageContent(message_text=make_unit(1930))
    )

    results.append(petuch)
    results.append(group)
    results.append(vzvod)
    results.append(rota)
    results.append(batalion)
    results.append(polk)
    results.append(brigada)
    print(query)
    log = open('log.txt', 'a')
    log.write(str(query)+'\n')
    log.close()
    bot.answer_inline_query(query.id, results)

if __name__ == '__main__':
    bot.polling(none_stop=True)