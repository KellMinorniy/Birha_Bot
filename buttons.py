import telebot

# Кнопка /start

def startButtons(onAuth, onRoot):
    inline_keyboard = telebot.types.InlineKeyboardMarkup()

    buttonOrder = telebot.types.InlineKeyboardButton('Я заказчик', callback_data='order')
    buttonExecutor = telebot.types.InlineKeyboardButton('Я исполнитель', callback_data='executor')

    buttonAdminPanel = telebot.types.InlineKeyboardButton('Админ-Панель', callback_data='admin-Panel')

    buttonProfile = telebot.types.InlineKeyboardButton('Профиль', callback_data='profile')
    buttonOrderList = telebot.types.InlineKeyboardButton('Список заказов', callback_data='order-list')
    buttonSettings = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')
   
    if onAuth == True:
        inline_keyboard.add(buttonProfile, buttonOrderList, buttonSettings)
    elif onRoot == True:
        inline_keyboard.add(buttonProfile, buttonOrderList, buttonSettings, buttonAdminPanel)
    else:
        inline_keyboard.add(buttonExecutor, buttonOrder)    
   
    return inline_keyboard

# Кнопка "Назад"

def backButtons():
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
    buttonBack= telebot.types.InlineKeyboardButton('Вернутся назад', callback_data='backToMenu')
    inline_keyboard.add(buttonBack)  

    return inline_keyboard