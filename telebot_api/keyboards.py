import json


class toJsonClass:

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=3)

class Button(toJsonClass):

    def set_attr(self, prop, val):
        setattr(self, prop, val)

class ReplyKeyboardMarkup(toJsonClass):
    
    def __init__(self, resize_keyboard=False, one_time_keyboard=False, selective=False):
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.keyboard = []

    def row(self, buttons):
        self.keyboard.append(buttons)

class KeyboardButton(Button):
    
    def __init__(self, text, **kwargs):
        self.text = text
        for k, v in kwargs.keys():
            self.set_attr(k, v)

class InlineKeyboardMarkup(toJsonClass):

    def __init__(self):
        self.inline_keyboard = []

    def row(self, buttons):
        self.inline_keyboard.append(buttons)

class InlineKeyboardButton(Button):

    def __init__(self, text, **kwargs):
        self.text = text
        for k, v in kwargs.items():
            self.set_attr(k, v)

class ReplyKeyboardRemove(toJsonClass):

    def __init__(self):
        self.remove_keyboard = True









