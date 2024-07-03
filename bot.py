import telebot
from config import TOKEN, HOST_DATABASE_HOST, HOST_DATABASE_USERNAME, HOST_DATABASE_PASSWORD, HOST_DATABASE_NAME
import mysql.connector
from response import response
from core import dataBaseRequest
from buttons import * 



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
    if len(dataBaseRequest(f"SELECT * FROM `users` WHERE `chatID` = '{message.chat.id}'")) == 0:
        dataBaseRequest(f"INSERT INTO `users`(`username`, `chatID`) VALUES ('{message.from_user.username}','{message.chat.id}')")
        
       
        bot.send_message(message.chat.id, response['StartMessage'], reply_markup=startButtons(0,0))
    else:
        bot.send_message(message.chat.id, response['StartMessageAuth'], reply_markup=startButtons(1,0))



# Тут пока костыльно - для тестов

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    text = 'Вы выбрали: '
    if call.data == 'order':
        status = 'order'
        dataBaseRequest(f"UPDATE `users` SET `status` = '{status}' WHERE `chatID` = '{call.message.chat.id}'")
    elif call.data == 'executor':
        status = 'executor'
        dataBaseRequest(f"UPDATE `users` SET `status` = '{status}' WHERE `chatID` = '{call.message.chat.id}'")
    elif call.data == 'profile':
        bot.send_message(call.message.chat.id, 'Тут профиль', reply_markuзp=backButtons())

    
    print(call.message.chat.id)
    bot.answer_callback_query(callback_query_id=call.id, text=text, show_alert=False)

bot.polling(none_stop=True)