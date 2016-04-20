import logging
from pymongo import MongoClient


class MongoConnect(object):
    """Maintaining some basic functions for pymongo"""
    def __init__(self, mongo_host, mongo_port, mongo_db,
                 mongo_username=None, mongo_password=None, mechanism=None):
        super(MongoConnect, self).__init__()
        self.LOG = logging.getLogger(__name__)
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_username = mongo_username
        self.mongo_password = mongo_password
        if mechanism is not None:
            self.mechanism = mechanism
        else:
            self.mechanism = 'DEFAULT'
        self.client = None
        self.db = None

    def open_connection(self):
        self.LOG.debug("Openning Connection...")
        try:
            self.client = MongoClient(host=self.mongo_host,
                                      port=self.mongo_port)
            self.db = self.client[self.mongo_db]

            if self.mongo_username and self.mongo_password:
                self.db.authenticate(self.mongo_username, self.mongo_password,
                                     self.mechanism)
        except Exception as e:
            self.LOG.exception("Fail openning connection to database")
            raise e

    def close_connection(self):
        self.LOG.debug("Closing Connection...")
        self.client.close()
        self.client = None
        self.db = None

    def get_data(self, collection, query=None):
        self.LOG.debug(
            "Getting data from %s with query %s",
            collection, str(query))

        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]

            if query:
                res = db[collection].find(query)
            else:
                res = db[collection].find()

            return list(res)

    def get_data_by_id(self, collection, _id):
        self.LOG.debug(
            "Getting data from %s with _id = %s",
            collection, str(_id))

        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]

            res = db[collection].find_one({"_id": _id})

    def insert(self, collection, data):
        self.LOG.debug(
            "Doing insert to %s with nData=%d",
            collection, len(data))

        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]
            res = db[collection].insert_many(data)
            return res

    def upsert(self, collection, filter, update):
        self.LOG.info(
            "Doing upsert to %s with filter %s",
            collection, str(filter))

        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]

            res = db[collection].update_one(
                filter,
                update,
                upsert=True)

            return res

    def bulk_upsert(self, collection, data):
        """
        `data` must be a tuple.
        example:
        >>> data = [
        ...     ({"_id": 1}, {"$set": {"name": "Andrew"}}),
        ...     ({"_id": 2}, {"$set": {"age": 17}})]

        """
        self.LOG.info("Doing bulk upsert to %s", collection)

        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]

            bulk = db[collection].initialize_unordered_bulk_op()

            for query, update in data:
                bulk.find(query).upsert().update(update)

            res = bulk.execute()

            return res

    def delete(self, collection, query):
        self.LOG.info("Delete from %s with query: %s", collection, str(query))
        with MongoClient(host=self.mongo_host,
                         port=self.mongo_port) as client:
            db = client[self.mongo_db]

            res = db[collection].remove(query)

            return res
