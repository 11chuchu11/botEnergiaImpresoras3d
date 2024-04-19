import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, f"chat id: {message.chat.id}")

if __name__ == "__main__":
    bot.polling(none_stop=True)