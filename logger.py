import logging
import logging.handlers

def setup_logger(log_file='app.log', log_level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger setup complete.')