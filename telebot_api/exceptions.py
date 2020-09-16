class Error(Exception):
    
    def __init__(self, message):
        self.message = message

class sendMessageError(Error):
    pass

class getUpdatesError(Error):
    pass

class setWebhookError(Error):
    pass

class removeWebhookError(Error):
    pass

class useWebhookError(Error):
    pass
