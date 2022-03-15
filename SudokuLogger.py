import logging
import enum


class SudokuLogType(enum.Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class SudokuLogger:
    def __init__(self, filename):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')
        self.file_handle = logging.FileHandler(filename)
        self.file_handle.setLevel(logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %H:%M:%S')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def write_log(self, message, log_type=SudokuLogType.DEBUG):
        if log_type == SudokuLogType.DEBUG:
            self.logger.debug(message)
        elif log_type == SudokuLogType.INFO:
            self.logger.info(message)
        elif log_type == SudokuLogType.WARNING:
            self.logger.warning(message)
        elif log_type == SudokuLogType.ERROR:
            self.logger.error(message)
        elif log_type == SudokuLogType.CRITICAL:
            self.logger.critical(message)
