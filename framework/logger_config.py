import logging


def setup_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)  # Показывать только INFO и выше

    return logger
