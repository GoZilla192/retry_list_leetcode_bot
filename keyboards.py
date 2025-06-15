import telebot


def get_inline_main_menu():
	keyboard = telebot.types.InlineKeyboardMarkup()
	buttons = [
		telebot.types.InlineKeyboardButton("Retry List", callback_data="retry_list"),
	]
	
	keyboard.add(*buttons)

	return keyboard


def get_inline_menu_retry_list():
	keyboard = telebot.types.InlineKeyboardMarkup()
	buttons = [
		telebot.types.InlineKeyboardButton("Add problem", callback_data="add_problem_to_retry_list"),
		telebot.types.InlineKeyboardButton("My problems", callback_data="#"),
		telebot.types.InlineKeyboardButton("Back to main menu", callback_data="back_to_main_menu"),
	]
	
	keyboard.add(*buttons)
	
	return keyboard