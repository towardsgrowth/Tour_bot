from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def phone_button(name):
    markup  = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(name, request_contact=True)
    markup.add(btn)
    return markup


def make_buttons(names: list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for name in names:
        btn = KeyboardButton(name)
        markup.add(btn)
    return markup

