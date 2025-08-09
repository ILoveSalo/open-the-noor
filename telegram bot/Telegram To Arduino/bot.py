import os
import time
from dotenv import load_dotenv
import telebot
import serial

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN was not found!")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['open'])
def send_welcome(message):
    bot.reply_to(message, "Opening the gate...")
    ser.write(b'1')

@bot.message_handler(commands=['close'])
def send_welcome(message):
    bot.reply_to(message, "Closing the gate...")
    ser.write(b'0')

ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

bot.infinity_polling()