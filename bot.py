import telebot
from telebot import types

tokken = '6209685837:AAH_s2KXvXqCpKHi3HZ5838UeaOFdais1T4'
bot = telebot.TeleBot(tokken)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  chat_id = message.chat.id
  bot.send_message(chat_id, "Привет, я твой телеграм-бот!")

@bot.message_handler(commands = ['site'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://faticc.github.io')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт", reply_markup = markup)

@bot.message_handler(commands=['hello'])
def send_hello(message):
  chat_id = message.chat.id
  all_users = bot.get_chat_members_count(chat_id)
  bot.send_message(chat_id, f"Привет всем! У нас тут {all_users} участников в чате!")

bot.polling(none_stop=True, interval=0)