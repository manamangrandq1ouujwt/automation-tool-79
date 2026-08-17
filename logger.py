import logging


def setup_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def log_info(logger, message):
    logger.info(message)


def log_warning(logger, message):
    logger.warning(message)


def log_error(logger, message):
    logger.error(message)


if __name__ == '__main__':
    test_logger = setup_logger('TestLogger')
    log_info(test_logger, 'This is an info message.')
    log_warning(test_logger, 'This is a warning message.')
    log_error(test_logger, 'This is an error message.')