import requests
from urllib.parse import urlencode


class API:

    api_link = 'https://api.telegram.org/bot{token}/{method}?'
    
    def __init__(self, token):
        self.token = token

    def send_message(self, chat_id, text):
        params = {}
        params['chat_id'] = chat_id
        params['text'] = text

        link = self.api_link.format(token=self.token, method='sendMessage') + urlencode(params)

        headers = {}
        headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

        requests.get(url=link, headers=headers)
