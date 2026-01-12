import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	keyboard = telebot.types.ReplyKeyboardMarkup()
	keyboard.add(
		telebot.types.KeyboardButton('Взять книгу'),
		telebot.types.KeyboardButton('Вернуть книгу')
	)
	keyboard.add(
		telebot.types.KeyboardButton('Забронировать книгу'),
		telebot.types.KeyboardButton('Найти книгу'),
	)
	bot.reply_to(message, 'Привет! Это бот библиотеки. Что ты хочешь сделать?', reply_markup=keyboard)



@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
