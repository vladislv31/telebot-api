from telebot_api import API, keyboards
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

@bot.message_handler('/keyb')
def start_message(m):
    cid = m['chat']['id']
    keyboard = keyboards.ReplyKeyboardMarkup(resize=True)
    btn = keyboards.KeyboardButton('hello')
    keyboard.row([btn])
    bot.send_message(cid, 'info message', reply_markup=keyboard)

@bot.message_handler('/hide')
def start_message(m):
    cid = m['chat']['id']
    keyboard = keyboards.ReplyKeyboardRemove()
    bot.send_message(cid, 'info message', reply_markup=keyboard)

bot.watching()

