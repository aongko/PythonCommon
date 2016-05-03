# PythonCommon

Some basic functionality to help ease the pain. Well, not pain, actually.

## Installation ##

To install, run:

    python3 setup.py install


## Usage

For database connection to MongoDB using PyMongo:

```python

  >>> from databasefunction import MongoConnect
  >>> mongo = MongoConnect("127.0.0.1", 27017, "database_name")

```

For database connection to MySQL using PyMySQL:

```python
  >>> from databasefunction import MysqlConnect
  >>> mysql = MysqlConnect("127.0.0.1", 3306, "aongko", "password", "database_name")

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
  >>> LanguageDetector().detect("some text we want to know the language")
  'en'

```

For Slack notifier:

```python
  >>> from notifier import SlackNotifier
  >>> notifier = SlackNotifier(url="some_valid_url", channel="#channel-name", username="username", debug=False)
  >>> notifier.notify("some message")

```
