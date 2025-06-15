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
		telebot.types.InlineKeyboardButton("1", callback_data="#"),
		telebot.types.InlineKeyboardButton("2", callback_data="#"),
		telebot.types.InlineKeyboardButton("3", callback_data="#"),
		telebot.types.InlineKeyboardButton("Back to main menu", callback_data="back_to_main_menu"),
	]
	
	keyboard.add(*buttons)
	
	return keyboard