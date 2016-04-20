import logging
import pymysql


class MysqlConnect(object):
    """Maintaining some basic functions for PyMySQL"""
    def __init__(self, mysql_host, mysql_port,
                 mysql_username, mysql_password,
                 mysql_database):
        super(MysqlConnect, self).__init__()
        self.LOG = logging.getLogger(__name__)
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_username = mysql_username
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

    def open_connection(self):
        self.LOG.debug("Openning Connection...")
        try:
            self.connection = pymysql.connect(
                host=self.mysql_host,
                port=self.mysql_port,
                user=self.mysql_username,
                password=self.mysql_password,
                db=self.mysql_database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            self.cursor = self.connection.cursor()
        except Exception as e:
            self.LOG.exception("Fail openning connection to database")
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
        connection = pymysql.connect(host=self.mysql_host,
                                     port=self.mysql_port,
                                     user=self.mysql_username,
                                     password=self.mysql_password,
                                     db=self.mysql_database,
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
