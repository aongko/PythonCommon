# PythonCommon

Some basic functionality to help ease the pain. Well, not pain, actually.

## Installation ##

To install, run:

    python3 setup.py install


## Usage

For database connection to MongoDB using PyMongo:

```python
  >>> from databasefunction import MongoConfig
  >>> mongo_config = MongoConfig(host="172.0.0.1", port=27017, database="database_name")
  >>> from databasefunction import MongoConnect
  >>> mongo = MongoConnect(mongo_config)
```

For database connection to MySQL using PyMySQL:

```python
  >>> from databasefunction import MysqlConfig
  >>> mysql_config = MysqlConfig(host="127.0.0.1", port=3306, username="aongko", password="password", database="database_name")
  >>> from databasefunction import MysqlConnect
  >>> mysql = MysqlConnect(mysql_config)
```

For logging setup:

```python
  >>> from pythonlogger import setup_logging
  >>> setup_logging("DEBUG",
  ...               base_dir="/home/user/",
  ...               directory="log",
  ...               filename="logname")
  >>> import logging
  >>> logging.getLogger(__name__)
```

For language detection:

```python
  >>> from text_processing import LanguageDetector
  >>> LanguageDetector.detect("some text we want to know the language")
  'en'
```

For Slack notifier:

```python
  >>> from notifier import SlackNotifier
  >>> notifier = SlackNotifier(url="some_valid_url", channel="#channel-name", username="username", debug=False)
  >>> notifier.notify("some message")
```
