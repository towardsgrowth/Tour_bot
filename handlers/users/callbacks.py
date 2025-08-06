from telebot.types import CallbackQuery
from data.loader import bot

@bot.callback_query_handlers(func= lambda call: call.data in ["uz", "en", "ru"])
def reaction_lang(call:CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
