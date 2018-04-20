import logging
import logging.config
from os import path  # Logging configuration


def config_logging():

    log_file = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(log_file)

    # create logger
    logger = logging.getLogger(__name__)
    # Log for import
    logger.info('Logging configured.')

    return logger
