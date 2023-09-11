import logging


class LogGenerator:

    @staticmethod
    def generateLogger():
        logging.basicConfig(filename="../Backend/logs/backend_automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
