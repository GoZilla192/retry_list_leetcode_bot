def start_handler(bot, message):
	message_to_send = "Hi, I'm a bot that'll help you level up in <b>Leetcode</b>.\n\nIt's simple, you research the problem, send it to me and I'll remind you to do it again after a time.\n\nClick the button to add the Problem ↙️"
	bot.send_message(message.chat.id, message_to_send, parse_mode="html")
	