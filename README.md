# PythonCommon

Some basic functionality to help ease the pain. Well, not pain, actually.

## Installation ##

To install, run:

    python3 setup.py install


## Usage

For database connection to MongoDB using PyMongo:

```python

  >>> from databasefunction.mongoconnect import MongoConnect
  >>> mongo = MongoConnect("127.0.0.1", 27017, "database_name")
```

For database connection to MySQL using PyMySQL:

```python
  >>> from databasefunction.mysqlconnect import MysqlConnect
  >>> mysql = MysqlConnect("127.0.0.1", 3306, "aongko", "password", "database_name")
```

For logging setup:

```python
  >>> from pythonlogger.pythonlogger import setup_logging
  >>> setup_logging("DEBUG",
  ...               base_dir="/home/user/",
  ...               directory="log",
  ...               filename="logname")
  >>> import logging
  >>> logging.getLogger(__name__)

```
