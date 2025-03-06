import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic
from model import get_class
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("#")



















# Запускаем бота
bot.polling()