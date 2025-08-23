import logging


def get_sdk_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(logging.NullHandler())  # safe default
    logger.propagate = True
    return logger
