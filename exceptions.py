class CustomError(Exception):
    pass

class NetworkError(CustomError):
    def __init__(self, message='Network connection error'):
        self.message = message
        super().__init__(self.message)

class InvalidResponseError(CustomError):
    def __init__(self, message='Received an invalid response'):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(CustomError):
    def __init__(self, message='Insufficient funds for the transaction'):
        self.message = message
        super().__init__(self.message)

class RateLimitExceededError(CustomError):
    def __init__(self, message='Rate limit exceeded, please try again later'):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(CustomError):
    def __init__(self, message='Authentication failed, check your credentials'):
        self.message = message
        super().__init__(self.message)