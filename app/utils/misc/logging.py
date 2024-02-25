import logging

main_logging_format = "%(asctime)s\t\t%(levelname)s\t\t%(threadName)s\t\t%(filename)s\t\t%(message)s"
logging.basicConfig(format=main_logging_format, level=logging.INFO)
