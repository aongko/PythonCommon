import logging.config
import os


def setup_logging(level="DEBUG",
                  base_dir=None, directory="log",
                  filename=None, log_format=None, log_config=None):
    """
    A convenient way to configure your logger.

    """

    if filename is None:
        filename = "log"

    if base_dir is None:
        base_dir = ""

    if not base_dir.endswith('/'):
        base_dir += "/"

    filename = base_dir + directory + "/" + filename + ".log"

    if not os.path.exists(base_dir + directory):
        os.makedirs(base_dir + directory)

    fmt = '%(asctime)s-[%(levelname)-8s]-%(name)-30s: %(message)s'
    if log_format is not None:
        fmt = log_format

    configured_log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': fmt
            },
        },
        'handlers': {
            'default': {
                'level': "DEBUG",
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': filename,
                'when': 'midnight',
                'formatter': 'standard',
                'encoding': 'utf-8'
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': level,
                'propagate': True
            }
        }
    }

    if log_config is not None:
        configured_log_config = log_config

    logging.config.dictConfig(configured_log_config)
