def start_logger():
    from logging import getLogger, FileHandler, StreamHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL

    # create logger
    logger = getLogger('programmer')
    logger.setLevel(DEBUG)

    # create console handler and set level to debug
    # handler = StreamHandler()
    handler = FileHandler("programmer.log")
    handler.setLevel(CRITICAL)
    # create formatter
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    handler.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(handler)

    # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    return logger