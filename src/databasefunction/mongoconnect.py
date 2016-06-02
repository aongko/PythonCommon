import logging
from pymongo import MongoClient
from .mongoconfig import MongoConfig


class MongoConnect:
    """Maintaining some basic functions for pymongo"""

    def __init__(self, mongo_config=MongoConfig()):
        self.LOG = logging.getLogger(self.__class__.__name__)

        self.mongo_config = mongo_config

        self.client = None
        self.db = None

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
            self.client = MongoClient(host=self.mongo_config.host,
                                      port=self.mongo_config.port)
            self.db = self.client[self.mongo_config.database]

            if self.mongo_config.username and self.mongo_config.password:
                self.db.authenticate(self.mongo_config.username,
                                     self.mongo_config.password,
                                     self.mongo_config.mechanism)
        except Exception as e:
            self.LOG.exception("Fail opening connection to database")
            raise e

    def close_connection(self):
        self.LOG.debug("Closing Connection...")
        self.client.close()
        self.client = None
        self.db = None

    def get_data(self, collection, query=None, projection=None):
        self.LOG.debug(
            "Getting data from %s with query %s and projection %s",
            collection, str(query), str(projection))

        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]
            res = db[collection].find(filter=query, projection=projection)
            return list(res)

    def get_data_by_id(self, collection, _id):
        self.LOG.debug(
            "Getting data from %s with _id = %s",
            collection, str(_id))

        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]
            res = db[collection].find_one({"_id": _id})
            return list(res)

    def insert(self, collection, data):
        self.LOG.debug(
            "Doing insert to %s with nData=%d",
            collection, len(data))

        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]
            res = db[collection].insert_many(data)
            return res

    def upsert(self, collection, query, update):
        self.LOG.info(
            "Doing upsert to %s with filter %s",
            collection, str(query))

        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]

            res = db[collection].update_one(
                query,
                update,
                upsert=True)

            return res

    def bulk_upsert(self, collection, data):
        """
        `data` must be a tuple.
        example:

        data = [
           ({"_id": 1}, {"$set": {"name": "Andrew"}}),
           ({"_id": 2}, {"$set": {"age": 17}})]

        """
        self.LOG.info("Doing bulk upsert to %s", collection)

        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]

            bulk = db[collection].initialize_unordered_bulk_op()

            for query, update in data:
                bulk.find(query).upsert().update(update)

            res = bulk.execute()

            return res

    def delete(self, collection, query):
        self.LOG.info("Delete from %s with query: %s", collection, str(query))
        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]

            res = db[collection].remove(query)

            return res

    def aggregate(self, collection, pipeline):
        with MongoClient(host=self.mongo_config.host,
                         port=self.mongo_config.port) as client:
            db = client[self.mongo_config.database]
            res = db[collection].aggregate(pipeline)
            return list(res)
