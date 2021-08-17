import logging
class logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('Logger.log')
    format = '%(asctime)s : %(created)f : %(name)s : %(filename)s : %(levelname)s : %(message)s'
    formatter = logging.Formatter(format)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)