from telebot_api import API, keyboards
import config
import time


bot = API(config.TOKEN)
bot.config['webhook_host'] = 'https://d0a1fe3048b2.ngrok.io'

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
    keyboard = keyboards.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = keyboards.KeyboardButton('hello')
    keyboard.row([btn])
    bot.send_message(cid, 'info message', reply_markup=keyboard)

@bot.message_handler('/inline')
def start_message(m):
    cid = m['chat']['id']
    keyboard = keyboards.InlineKeyboardMarkup()
    btn = keyboards.InlineKeyboardButton('hello', callback_data='https://google.com')
    keyboard.row([btn])
    bot.send_message(cid, 'info message', reply_markup=keyboard)

@bot.message_handler('/hide')
def start_message(m):
    cid = m['chat']['id']
    keyboard = keyboards.ReplyKeyboardRemove()
    bot.send_message(cid, 'info message', reply_markup=keyboard)

@bot.message_handler('/parse_mode')
def start_message(m):
    cid = m['chat']['id']
    reply = """*bold text*
    _italic text_
    [inline URL](http://www.example.com/)
    [inline mention of a user](tg://user?id=463758574)
    `inline fixed-width code`
    ```
    pre-formatted fixed-width code block
    ```
    ```python
    pre-formatted fixed-width code block written in the Python programming language
    ```"""
    bot.send_message(cid, reply, parse_mode='MarkdownV2')

@bot.message_handler('/get_id')
def start_message(m):
    cid = m['chat']['id']
    bot.send_message(cid, str(cid))
    bot.register_next_step_handler(cid, print_text)

def print_text(m):
    cid = m['chat']['id']
    bot.send_message(cid, 'how are you?')
    bot.register_next_step_handler(cid, how_are)

def how_are(m):
    cid = m['chat']['id']
    bot.send_message(cid, 'Cool ' + m['text'])


#bot.remove_webhook()
#time.sleep(1)
#bot.set_webhook('http://c7d51034d510.ngrok.io')

#bot.use_webhook()

bot.watching()
