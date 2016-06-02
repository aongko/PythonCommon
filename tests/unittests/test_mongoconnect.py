import unittest
from databasefunction import MongoConnect
from unittest.mock import create_autospec
from unittest.mock import MagicMock


class TestMongoConnect(unittest.TestCase):
    def setUp(self):
        self.mongo = MongoConnect()
        self.mongo.mongo_config.host = "127.0.0.1"
        self.mongo.mongo_config.port = 27017

    def tearDown(self):
        self.mongo = None

    def test_open_connection(self):
        self.mongo.open_connection()
        self.assertIsNotNone(self.mongo.client)
        self.assertIsNotNone(self.mongo.db)

    def test_close_connection_without_open_connection(self):
        with self.assertRaises(AttributeError):
            self.mongo.close_connection()

    def test_close_connection_with_open_connection(self):
        self.mongo.open_connection()
        self.mongo.close_connection()
        self.assertIsNone(self.mongo.client)
        self.assertIsNone(self.mongo.db)

    def test_get_data(self):
        data = [
            {"id": 1, "name": "a"},
            {"id": 2, "name": "b"},
            {"id": 3, "name": "c"},
            {"id": 4, "name": "d"},
            {"id": 5, "name": "e"},
        ]
        mock_db = self.mongo
        mock_db.get_data = MagicMock(return_value=data)
        result = mock_db.get_data("test_collection", {}, None)
        mock_db.get_data.assert_called_once_with("test_collection", {}, None)
        self.assertEqual(result, data)

    def test_get_data_by_id(self):
        data = {"_id": 123, "name": "xyz"}
        mock_db = create_autospec(MongoConnect)
        mock_db.get_data_by_id = MagicMock(return_value=[data])
        result = mock_db.get_data_by_id("test_collection", 123)
        mock_db.get_data_by_id.assert_called_once_with("test_collection", 123)
        self.assertEqual(result, [data])

    def test_get_data_by_id_without_id(self):
        data = {"_id": 123, "name": "xyz"}
        mock_db = create_autospec(MongoConnect)
        with self.assertRaisesRegex(TypeError, "missing a required argument: '_id'") as e:
            mock_db.get_data_by_id("test_collection")

    # def test_insert(self):
    #     self.fail()
    #
    # def test_upsert(self):
    #     self.fail()
    #
    # def test_bulk_upsert(self):
    #     self.fail()
    #
    # def test_delete(self):
    #     self.fail()
    #
    # def test_aggregate(self):
    #     self.fail()

if __name__ == "__main__":
    unittest.main()
