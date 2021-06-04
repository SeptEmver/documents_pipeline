from abc import ABC


class RequestError(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.status_code = status_code

    def get_status_code(self):
        return self.status_code


class ClientError(RequestError):
    def __init__(self, message):
        super().__init__(message)
        self.status_code = 400


class ServerError(RequestError):
    def __init__(self, message):
        super().__init__(message)
        self.status_code = 500
