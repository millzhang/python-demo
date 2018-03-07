import logging
import logging.config


class Logger():
    def __init__(self, name):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger('name')
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler('log.log')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.logger = logger

    def debug(self, info):
        self.logger.debug(info)
