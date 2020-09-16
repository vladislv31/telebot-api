import json
import time
from telebot_api.functions import get_request, json_decode, random_str
from telebot_api.exceptions import sendMessageError, getUpdatesError, setWebhookError, removeWebhookError, useWebhookError
from webob import Request, Response


class API:

    api_link = 'https://api.telegram.org/bot{token}/{method}'
    handlers = {}
    
    def __init__(self, token):
        self.token = token
        self.webhook_uri = self.generate_webhook_uri()
        self.config = {}

    def __call__(self, environ, start_response):
        request = Request(environ)

        current_uri = request.path

        if current_uri == self.webhook_uri:
            j = request.body
            update = json_decode(j)
            self.process_updates([update])
            
        response = Response()
        response.text = 'ok'

        return response(environ, start_response)

    def message_handler(self, text):
        def wrapper(handler):
            self.handlers[text] = handler
            return handler

        return wrapper
    
    def api_command(self, command, params={}):
        link = self.api_link.format(token=self.token, method=command)
        r = get_request(link, params)
        return json_decode(r.text)

    def send_message(self, chat_id, text, reply_markup=None):
        params = {}

        params['chat_id'] = chat_id
        params['text'] = text
        if reply_markup:
            params['reply_markup'] = reply_markup.toJSON()

        j = self.api_command('sendMessage', params)

        if j['ok'] is True:
            return j['result']
        else:
            raise sendMessageError(j['description'])

    def get_updates(self, offset=100, limit=100):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        j = self.api_command('getUpdates', params)

        if j['ok'] is True:
            return j['result']
        else:
            raise getUpdatesError(j['description'])

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
            try:
                updates = self.get_updates(offset=update_id)
                if updates:
                    update_id = self.process_updates(updates) + 1
            except KeyboardInterrupt:
                exit()

    def generate_webhook_uri(self):
        return '/' + random_str(25)

    def set_webhook(self, url, cert=None):
        params = {}
        params['url'] = url + self.webhook_uri

        j = self.api_command('setWebhook', params)

        if j['ok'] is True:
            return j['result']
        else:
            raise setWebhookError(j['description'])

    def remove_webhook(self):
        j = self.api_command('deleteWebhook')

        if j['ok'] is True:
            return j['result']
        else:
            raise removeWebhookError(j['description'])

    def use_webhook(self):
        self.remove_webhook()
        time.sleep(0.5)
        try:
            self.set_webhook(self.config['webhook_host'])
        except:
            raise useWebhookError('\'webhook_host\' key are not exists in config dict.')









