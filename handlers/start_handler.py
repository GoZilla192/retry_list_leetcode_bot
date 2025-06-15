import telebot


def start_handler(bot, message, keyboard_markup):
	# message_to_send = "Hi, I'm a bot that'll help you level up in <b>Leetcode</b>.\n\nIt's simple, you research the problem, send it to me and I'll remind you to do it again after a time.\n\nClick the button to add the Problem ↙️"
	message_to_send = "Hi, I'm a bot that'll help you level up in <b>Leetcode</b>.\nChoice option:"
	bot.send_message(message.chat.id, message_to_send, parse_mode="html", reply_markup=keyboard_markup)
	