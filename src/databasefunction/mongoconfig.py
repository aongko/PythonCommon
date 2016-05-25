class MongoConfig(object):
    """config to be used alongside MongoConnect"""

    DEFAULT_HOST = "127.0.0.1"
    DEFAULT_PORT = 27017
    DEFAULT_DATABASE = "test"
    DEFAULT_USERNAME = None
    DEFAULT_PASSWORD = None
    DEFAULT_MECHANISM = "DEFAULT"

    def __init__(self, host=None, port=None, database=None,
                 username=None, password=None, mechanism=None):
        super(MongoConfig, self).__init__()
        self.host = host if host else self.DEFAULT_HOST
        self.port = port if port else self.DEFAULT_PORT
        self.database = database if database else self.DEFAULT_DATABASE

        self.username = username if username else self.DEFAULT_USERNAME
        self.password = password if password else self.DEFAULT_PASSWORD
        self.mechanism = mechanism if mechanism else self.DEFAULT_MECHANISM
