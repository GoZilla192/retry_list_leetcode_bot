import telebot
from dotenv import load_dotenv
import os

from handlers import start_handler, help_handler

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message: telebot.types.Message):
	start_handler(bot, message)


@bot.message_handler(commands=["help"])
def handle_help(message: telebot.types.Message):
	help_handler(bot, message)


if __name__ == "__main__":
	bot.infinity_polling()
	