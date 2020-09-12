import json
import time
from telebot_api.functions import get_request


class API:

    api_link = 'https://api.telegram.org/bot{token}/{method}'
    handlers = {}
    
    def __init__(self, token):
        self.token = token

    def message_handler(self, text):
        def wrapper(handler):
            self.handlers[text] = handler
            return handler

        return wrapper

    def send_message(self, chat_id, text):
        params = {}

        params['chat_id'] = chat_id
        params['text'] = text

        link = self.api_link.format(token=self.token, method='sendMessage')

        r = get_request(link, params)

        return json.loads(r.text)


    def get_updates(self, offset=100, limit=100):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        link = self.api_link.format(token=self.token, method='getUpdates')

        r = get_request(link, params)

        return json.loads(r.text)['result']

    def process_updates(self, updates):
        update_id = 0

        for u in updates:
            for text, handler in self.handlers.items():
                if u['message']['text'] == text:
                    handler(u['message'])
                    break
            update_id = u['update_id']

        return update_id

    def watching(self):
        update_id = -1

        while True:
            updates = self.get_updates(offset=update_id)
            if updates:
                update_id = self.process_updates(updates) + 1




