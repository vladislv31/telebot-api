from telebot_api import API
import config


bot = API(config.TOKEN)
#bot.send_message(463758574, 'test')

@bot.message_handler('/start')
def start_message(m):
    cid = m['chat']['id']
    bot.send_message(cid, 'start message')

@bot.message_handler('/info')
def start_message(m):
    cid = m['chat']['id']
    bot.send_message(cid, 'info message')

bot.watching()

