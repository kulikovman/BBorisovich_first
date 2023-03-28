import telebot
import setting

# telebot - https://pypi.org/project/pyTelegramBotAPI/


bot = telebot.TeleBot(setting.TOKEN)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text.lower() == 'да':
        bot.send_message(chat_id=message.chat.id, text="Пизда", reply_to_message_id=message.id)
    elif message.text.lower() == "нет":
        bot.send_message(chat_id=message.chat.id, text="Пидора ответ", reply_to_message_id=message.id)
    elif message.text.lower() == "da":
        bot.send_message(chat_id=message.chat.id, text="Pizda", reply_to_message_id=message.id)
    elif message.text.lower() == "net":
        bot.send_message(chat_id=message.chat.id, text="Pidora otvet", reply_to_message_id=message.id)
    elif message.text.lower() == "lf":
        bot.send_message(chat_id=message.chat.id, text="Gbplf", reply_to_message_id=message.id)
    elif message.text.lower() == "ytn":
        bot.send_message(chat_id=message.chat.id, text="Gbljhf jndtn", reply_to_message_id=message.id)


bot.polling(skip_pending=True)
