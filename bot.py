import telebot
from config import TOKEN, HOST_DATABASE_HOST, HOST_DATABASE_USERNAME, HOST_DATABASE_PASSWORD, HOST_DATABASE_NAME
import mysql.connector

bot = telebot.TeleBot(TOKEN)

# Подключение базы данных

connection = mysql.connector.connect(
  host = HOST_DATABASE_HOST,
  user = HOST_DATABASE_USERNAME,
  password = HOST_DATABASE_PASSWORD,
  database = HOST_DATABASE_NAME
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('Я заказчик', callback_data='order')
    button2 = telebot.types.InlineKeyboardButton('Я исполнитель', callback_data='executor')
    inline_keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Кто ты, воин?", reply_markup=inline_keyboard)




@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    text = 'Вы выбрали: '
    if call.data == 'order':
        text += 'Я заказчик'
    elif call.data == 'executor':
        text += 'Я исполнитель'
    bot.answer_callback_query(callback_query_id=call.id, text=text, show_alert=False)

bot.polling(none_stop=True)