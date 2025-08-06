from telebot import TeleBot
from config import Token
from database.database import Database


bot = TeleBot(Token)
db = Database()