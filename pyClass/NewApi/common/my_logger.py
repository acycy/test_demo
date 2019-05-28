

import logging
import configparser
from NewApi.common import project_path

class MyLogger(object):

    # def __init__(self):
    #     self.cf = configparser.ConfigParser()
    #     self.cf.read("log.conf", encoding="UTF-8")
    #     self.logger_name = self.cf.get("LOG", "logger_name")
    #     self.logger_level = self.cf.get("LOG", "logger_level")
    #     self.output_file_name = self.cf.get("LOG", "output_file_name'")
    #     self.output_file_level = self.cf.get("LOG", "output_file_level")
    #     self.formatter = self.cf.get("LOG", "formatter")

    def my_log(self, level, msg):
        my_logger = logging.getLogger("api_log")
        my_logger.setLevel("INFO")

        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')

        ch = logging.StreamHandler()
        ch.setLevel("INFO")
        ch.setFormatter(formatter)

        fh = logging.FileHandler(project_path.log_path, encoding="UTF-8")
        fh.setLevel("INFO")
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeFilter(fh)
        my_logger.removeFilter(ch)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def warning(self, msg):
        self.my_log("WARNING", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)


if __name__ == '__main__':
    my = MyLogger()
    my.error("报错了")