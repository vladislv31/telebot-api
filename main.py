from telebot_api import API
import config


bot = API(config.TOKEN)
bot.send_message(463758574, 'test')
