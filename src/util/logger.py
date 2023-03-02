"""
License: see attatched snippet
Copyright (c) 2023 Joshua Rose

This file is for everything that relates to the logging 
library with the condition that it is only calling functions
from said library.

If there are any bugs in this file, or any problems or issues,
pull requests are encouraged and highly appreciated.
"""

def setup_logger_object() -> object:
    """
    Description: This function is required (previously 
    wasn't a function and loaded in main() but due to handle_cli_args()
    function it needs to be loaded before everything as several messages
    are log calls in handle_cli_args()

    return: <object>
    """
    logging.config.fileConfig(locate_directory(file="config.ini"))
    logger: object = logging.getLogger()
    return logger

