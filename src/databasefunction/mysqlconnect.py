import logging
import pymysql
from .mysqlconfig import MysqlConfig


class MysqlConnect:
    """Maintaining some basic functions for PyMySQL"""

    def __init__(self, mysql_config=MysqlConfig()):
        self.LOG = logging.getLogger(self.__class__.__name__)

        self.mysql_config = mysql_config

        self.connection = None
        self.cursor = None

    def __getstate__(self):
        result = self.__dict__.copy()
        del result["LOG"]
        return result

    def __setstate__(self, state):
        self.__dict__ = state
        self.LOG = logging.getLogger(self.__class__.__name__)

    def open_connection(self):
        self.LOG.debug("Opening Connection...")
        try:
            self.connection = pymysql.connect(
                host=self.mysql_config.host,
                port=self.mysql_config.port,
                user=self.mysql_config.username,
                password=self.mysql_config.password,
                db=self.mysql_config.database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            self.cursor = self.connection.cursor()
        except Exception as e:
            self.LOG.exception("Fail opening connection to database")
            raise e

    def close_connection(self):
        self.LOG.debug("Closing Connection...")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

        self.connection = None
        self.cursor = None

    def get_data(self, sql, value=None):
        """Simple get data"""
        self.LOG.debug("Getting data...")
        connection = pymysql.connect(host=self.mysql_config.host,
                                     port=self.mysql_config.port,
                                     user=self.mysql_config.username,
                                     password=self.mysql_config.password,
                                     db=self.mysql_config.database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                if not value:
                    cursor.execute(sql)
                else:
                    cursor.execute(sql, value)

                result = cursor.fetchall()
        finally:
            connection.close()

        return result

    def query(self, query, value=None):
        """
        Execute a query

        """

        self.LOG.debug("Querying: %s", query)

        self.open_connection()
        self.cursor.execute(query, value)

        result = self.cursor.fetchall()

        self.close_connection()

        return result
