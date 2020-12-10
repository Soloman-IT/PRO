import telebot
from telebot import types
import time
bot = telebot.TeleBot("1440672540:AAFrd-ocdKRMesbhWI_GjU0ov-bf1kYGPLU")

markup_inline = types.InlineKeyboardMarkup()
film = types.InlineKeyboardButton(text = "ЖМЯК",callback_data = "film")
markup_inline.add(film)

@bot.message_handler(commands =["start"])
def start_bot(message):
	bot.send_message(message.chat.id,
		"""Привет😁 Меня зовут Руфи! Я твой защитник от скуки и однообразности 🥳🥳🥳
Моя сила в том, что я могу порекомендовать тебе рандомный фильм из 999 имеющихся у меня)""")
	bot.send_message(message.chat.id,
		"""Чтобы я выполнил свою титаническую работу жмякни сюда""", reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
	if call.data == "film":
		import project

		bot.send_message(call.message.chat.id,"Взламывается пентагон...")
		bot.send_message(call.message.chat.id,"Смотрим индусов с ютуба...")
		project.start()
		for i in range(4):
			if project.da[i].isdigit() == True and project.da[i].isalpha() ==False:
				bot.send_message(call.message.chat.id," :::: {0}".format(project.da[i]))
				print("        111111      ")
				continue
			if project.da[i].isalpha() == True and len(project.da[i]) > 55:
				bot.send_message(call.message.chat.id," :::: {0}".format(project.da[i]))
				continue	
			if project.da[i].isalpha() == True and len(project.da[i]) < 55:
				bot.send_message(call.message.chat.id," :::: {0}".format(project.da[i]))
				continue
			if project.da[i].isupper() == False:
				bot.send_message(call.message.chat.id," :::: {0}".format(project.da[i]))
				continue


@bot.message_handler(content_types=["text"])
def act(message):
	if message.text == "Взламывается пентагон...":
		bot.send_message(message.chat.id,"Название")

bot.polling()