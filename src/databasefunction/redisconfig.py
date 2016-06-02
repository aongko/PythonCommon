class RedisConfig:
    DEFAULT_HOST = "127.0.0.1"
    DEFAULT_PORT = 6379

    def __init__(self, host=None, port=None):
        self.host = host if host else self.DEFAULT_HOST
        self.port = port if port else self.DEFAULT_PORT
