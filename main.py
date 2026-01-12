import os
from dotenv import load_dotenv
import telebot
from core.library import Library

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


@bot.message_handler(regexp='Найти книгу')
def find_book(message):
	bot.reply_to(message, 'Введите ISBN книги для поиска')


@bot.message_handler(func=lambda message: message.text.isdigit())
def find_book_by_isbn(message):
	book = Library.get_book_by_isbn(message.text)
	reply = f'Название: {book['title']}\nАвторы: {''.join(book['authors'])}'
	bot.reply_to(message, reply)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
