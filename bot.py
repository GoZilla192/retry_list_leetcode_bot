import telebot
from dotenv import load_dotenv
import os

from handlers import start_handler, help_handler, retry_list_query_handler, main_menu_query_handler
from keyboards import get_inline_main_menu, get_inline_menu_retry_list

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message: telebot.types.Message):
	keyboard_markup = get_inline_main_menu()
	start_handler(bot, message, keyboard_markup)


@bot.message_handler(commands=["help"])
def handle_help(message: telebot.types.Message):
	help_handler(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: telebot.types.CallbackQuery):
	match call.data:
		case "retry_list":
			keyboard = get_inline_menu_retry_list()
			retry_list_query_handler(bot, call, keyboard)
		case "back_to_main_menu":
			keyboard = get_inline_main_menu()
			main_menu_query_handler(bot, call, keyboard)
		case "add_problem_to_retry_list":
			...
		case _:
			pass
	
	bot.answer_callback_query(call.id)


if __name__ == "__main__":
	bot.infinity_polling()
	