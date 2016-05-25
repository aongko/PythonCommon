class MysqlConfig(object):
    """config to be used along MysqlConnect"""

    DEFAULT_HOST = "127.0.0.1"
    DEFAULT_PORT = 3306
    DEFAULT_DATABASE = "test"
    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD = "admin123"

    def __init__(self, host=None, port=None,
                 username=None, password=None, database=None):
        super(MysqlConfig, self).__init__()
        self.host = host if host else self.DEFAULT_HOST
        self.port = port if port else self.DEFAULT_PORT
        self.username = username if username else self.DEFAULT_USERNAME
        self.password = password if password else self.DEFAULT_PASSWORD
        self.database = database if database else self.DEFAULT_DATABASE
