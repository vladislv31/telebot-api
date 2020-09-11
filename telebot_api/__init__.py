import requests
from urllib.parse import urlencode
import json
import time


class API:

    api_link = 'https://api.telegram.org/bot{token}/{method}?'
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

        link = self.api_link.format(token=self.token, method='sendMessage') + urlencode(params)

        headers = {}
        headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

        requests.get(url=link, headers=headers)

    def get_updates(self, offset=100, limit=100):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        link = self.api_link.format(token=self.token, method='getUpdates') + urlencode(params)

        headers = {}
        headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

        r = requests.get(url=link, headers=headers)

        return json.loads(r.text)['result']


    def watching(self):
        last_update = self.get_updates(-1)[0]
        update_id = last_update['update_id'] + 1 if last_update else 0
        print(update_id)

        while True:
            updates = self.get_updates(offset=update_id)
            print(update_id)
            print(updates)
            if updates:
                for u in updates:
                    for text, handler in self.handlers.items():
                        if u['message']['text'] == text:
                            handler(u['message'])
                            break
                    update_id = u['update_id'] + 1




