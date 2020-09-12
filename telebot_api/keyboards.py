import json


class toJsonClass:

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=3)

class ReplyKeyboardMarkup(toJsonClass):
    
    def __init__(self, resize=False, one_time=False, selective=False):
        self.resize_keyboard = resize
        self.one_time_keyboard = one_time
        self.selective = selective
        self.keyboard = []

    def row(self, buttons):
        self.keyboard.append(buttons)

class KeyboardButton(toJsonClass):
    
    def __init__(self, text):
        self.text = text

class ReplyKeyboardRemove(toJsonClass):

    def __init__(self):
        self.remove_keyboard = True









