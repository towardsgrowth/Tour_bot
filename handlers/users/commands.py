from telebot.types import Message

from config import TEXTS
from data.loader import bot, db
from handlers.users.callbacks import get_name
from keyboards.default import make_buttons
from keyboards.inline import lang_buttons

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    from_user_id = message.chat.id
    if not db.get_user(from_user_id):
        db.insert_telegram_id(from_user_id)
        text = (f"🇺🇿Assalomu alaykum FN30 tur agentligiga xush kelibsiz!!!\n"
            f"Iltimos tilni tanglang!!!\n\n"
            f"🇬🇧Hello, welcome to FN30 tour agency!!!\nPlease select the language!!!\n\n"
            f"🇷🇺Здравствуйте, добро пожаловать в туристическое агентство FN30!!!\nПожалуйста, выберите язык!!!")
        bot.send_message(chat_id, text, reply_markup=lang_buttons())
    else:
        lang  = db.get_lang(from_user_id)
        text  = TEXTS[lang][1]
        if None in db.get_user(from_user_id):
            msg = bot.send_message(chat_id, text)
            bot.register_next_step_handler(msg, get_name)
        else:
            names_buttons = TEXTS[lang][101]
            bot.send_message(chat_id, TEXTS[lang][4], reply_markup=make_buttons(names_buttons))
