from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def lang_buttons():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("O'zbek", callback_data="uz")
    btn2 = InlineKeyboardButton("English", callback_data="en")
    btn3 = InlineKeyboardButton("Russian", callback_data="ru")
    markup.add(btn1, btn2, btn3)
    return markup