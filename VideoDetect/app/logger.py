from loguru import logger

def setup_logger():
    logger.remove()
    logger.add("/home/kaan/PycharmProjects/VideoDetect/logs/app.log", rotation="500 MB",mode="w")
    return logger
