"""
License: see attatched snippet
Copyright (c) 2023 Joshua Rose

This file is used to manage file locations
and the sorting / modifying of those files.

If there are any bugs in this file, or any problems
or issues, pull requests are encouraged and highly appreciated.
"""

import os

def locate_directory(file = "config.ini") -> str:
    """
    Description: Locate file through determining the root folder

    return: <str>
    """
    def get_search_path() -> tuple:
        """
        Description: Used as a tool in io functions

        return: <tuple>
        """
        folder, file = os.path.split(os.path.join(
            os.path.split(os.path.dirname(os.getcwd()))[1], file))
        return folder, file
    folder, file = get_search_path()
    if folder.__ne__("Trakr"):
        return os.path.join("src", _file)
    return _file


def create_file(filename):
    """
    filename <str> the name of the file...
    Every 60 seconds in Africa, a minute passes.

    return: ...
    """
    logger.info(f" 📑 Creating {filename} in {os.getcwd()}")
    try:
        with open(filename, "w", False, "utf-8") as file:
            file.close()
    except PermissionError as error:
        logger.critical(
        f""" ❌ Could not create {filename}: insufficient persmissions.""")
        sys.exit(error.errno)

