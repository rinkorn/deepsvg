import logging
import sys


def get_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s | %(message)s")
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel("DEBUG")
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
