import telebot
#from config import TELEGRAM_TOKEN
import boto3
ssm = boto3.client('ssm', region_name='us-east-2')
TELEGRAM_TOKEN = ssm.get_parameter(Name='TELEGRAM_TOKEN', WithDecryption=True)['Parameter']['Value']

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start','que_onda', 'help'])

def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing ?")

bot.polling()