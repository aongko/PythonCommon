import logging.config
import os


def setup_logging(level="DEBUG",
                  base_dir=None, directory="log",
                  filename=None):
    if filename is None:
        filename = "log"

    if base_dir is None:
        base_dir = ""

    filename = base_dir + directory + "/" + filename + ".log"

    if not os.path.exists(base_dir + directory):
        os.makedirs(base_dir + directory)

    fmt = '%(asctime)s-[%(levelname)-8s]-%(name)-30s: %(message)s'

    log_config = {
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
                'formatter': 'standard'
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
    logging.config.dictConfig(log_config)
