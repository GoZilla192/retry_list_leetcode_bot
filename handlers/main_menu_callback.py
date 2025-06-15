import telebot


def main_menu_query_handler(bot, call: telebot.types.InlineQuery, keyboard_markup):
	message_to_send = "I'm a bot that'll help you level up in <b>Leetcode</b>.\nChoice option:"
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=message_to_send, parse_mode="html", reply_markup=keyboard_markup)
