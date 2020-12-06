import logging
import sys
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

FORMATTER = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
LOG_FILE = "app.log"


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_rotating_handler():
    rotating_handler = RotatingFileHandler(filename=LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5)
    rotating_handler.setFormatter(FORMATTER)
    return rotating_handler


def get_logger(logger_name=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.addHandler(get_rotating_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
