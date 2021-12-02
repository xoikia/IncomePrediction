import logging


class Logger:
    
    def __init__(self, file="applogs.txt"):
        self.filename = file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler(self.filename)
        self.file_handler.setLevel(logging.INFO)
        self.file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.file_handler)
        
    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg, error):
        self.logger.error("The following error occurred while {} {}".format(msg, error))