import requests
from urllib.parse import urlencode
import json
import random
import string


headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


def get_request(url, params={}):
    url += '?' + urlencode(params)
    r = requests.get(url=url, headers=headers)

    return r

def json_decode(j):
    return json.loads(j)

def json_encode(o):
    return json.dumps(o)

def random_str(l):
    symbols = string.ascii_lowercase
    result_str = ''.join(random.choice(symbols) for i in range(l))

    return result_str
