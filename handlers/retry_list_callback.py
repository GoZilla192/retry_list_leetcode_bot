import telebot


def retry_list_query_handler(bot: telebot.TeleBot, call: telebot.types.CallbackQuery, keyboard):
	bot.edit_message_text(
		chat_id=call.message.chat.id,
		message_id=call.message.id,
		text="Some logic retry list...",
		reply_markup=keyboard
	)