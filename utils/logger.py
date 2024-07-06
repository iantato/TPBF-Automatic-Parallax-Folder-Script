import logging
import types

def setup_logger(name: str):
    
    # Log formatter setup.
    formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)s] %(message)s",
                                  datefmt="%m/%d/%Y %H:%M:%S")
    blank_formatter = logging.Formatter(fmt="")
    
    # Log file handler.
    file_handler = logging.FileHandler(filename=f"{name}.log",
                                       mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Log printing handler.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    
    # Setup logger.
    logger = logging.getLogger('debug')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.file_handler = file_handler
    logger.console_handler = console_handler
    logger.formatter = formatter
    logger.blank_formatter = blank_formatter
    logger.newline = types.MethodType(log_newline, logger)

    logger.info('Successfuly initialized the logger.')

    return logger

# Change the formatter to blank so that we don't
# get the asctime when creating a new empty line.
def log_newline(self, how_many_lines: int = 1):
    
    self.file_handler.setFormatter(self.blank_formatter)
    self.console_handler.setFormatter(self.blank_formatter)

    for line in range(how_many_lines):
        self.info('')
    
    self.file_handler.setFormatter(self.formatter)
    self.console_handler.setFormatter(self.formatter)