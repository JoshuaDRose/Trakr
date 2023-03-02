"""
License: see attatched snippet
Copyright (c) 2023 Joshua Rose

The installer file is necessary to install dependencies required
for this project. It can be run with or without command line arguments,
however, these are developer features. More information on this is found 
in the handle_cli_args (name may and have may changed)

If there are any bugs in this file, or any problems issues and or pull
requests are encourage and highly appreciated.

submit a bug report: https://github.com/JoshuaDRose/Trakr/issues/new

TODO: 🪴 emoticons
TODO:    log folder
"""

import sys
import os
import json
import logging
import logging.config

args: set[str] = sys.argv[1:] # NOTE remove the first element on the right side
logger: None | object = None # Placeholder for logger object

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

def handle_cli_args():
    """
    Description: A file rarely needs change, but this
    allows developers the authority to do so in that case.

    :return:
    """

    @staticmethod
    def reset_install():
        """
        Description: I seldom use nested functions, but this is to minimize
        complexity when reading the file. I can look at handle_cli_args
        as one function; it need not be so complex.

        :return:
        """
        package_file = locate_directory(file="package.json")
        logger.debug(f" 📥 Writing a reset to {package_file}")

    if len(args):
        if len(args) >= 2:
            logger.warning(f" 🚧 Installer takes in <0 | 1> cli args")
        match args[0]:
            case "--reset-install":
                reset_install()

def load_dependency_as_object(file) -> object:
    """
    Description: This function serves as a dynamic way testing at
    runtime such that if a file not found error takes place it can
    be run again through being sourced rather than being continuously nested

    return: <object>
    """
    dependency_file_object: dict = json.load(open(dependency_file_name, "r"))
    return dependency_file_object
            
def load_dependencies(root) -> dict:
    """
    Description: Load file object from parent directory.

    return: <dict>
    """
    dependency_file_name: str = locate_directory(file="package.json")
    try:
        load_dependency_as_object(dependency_file_name)
    except FileNotFoundError:
        logger.warning(" 🔎 Could not find file - changing location")
        if 
        load_dependency_as_object(dependency_file_name)
    return dependency_file

def count_dependencies(file: dict) -> int:
    """
    Description: Counts the dependencies in file
    file: a json object loaded from a file
    
    return: <int>
    """
    dependency_amount = len(file.keys())
    return dependency_amount

def get_search_path() -> tuple:
    """
    Description: Used as a tool in io functions

    return: <tuple>
    """
    folder, _file = os.path.split(os.path.join(os.path.split(os.path.dirname(os.getcwd()))[1], file))
    return folder, file

def locate_directory(file = "config.ini") -> str:
    """
    Description: Locate file through determining the root folder

    return: <str>
    """
    folder, _file = os.path.split(os.path.join(os.path.split(os.path.dirname(os.getcwd()))[1], file))
    if folder.__ne__("Trakr"):
        return os.path.join("src", _file)
    return _file

def log_change(change: str, _file="install.log", emoji: str = str()) -> bool:
    """
    :change: message of the change to be recorded
    :emoji: unicode emoji character - NF allowed

    return: <true | false>
    """
    file = locate_directory(_file)
    # logger.debug("🥾 Removed un-needed variable: {file_content}", file_content=_file.__repr__())
    fp = object()
    try:
        fp = open(file, "a")
    except FileNotFoundError:
        _input = input(logger.debug(f" 🔎 Could not find {file}. Would you like to create a log file? [n/Y] >> "))
        try:
            match _input.lower():
                case "" | "yes" | "y":
                    with open(file, "w") as fp: fp.close()
                    logger.debug(f" ✅ Created {file} in {os.path.join(os.getcwd(), file)} ")
                    log_change(change, _file, emoji)
                    return
                case "n":
                    logger.debug("   Ignoring log file creation.")
                    return
                case _:
                    return
        except Exception as error:
            logger.critical(error)
            sys.exit(error.errno)

def create_file(filename):
    """
    filename <str> the name of the file... Every 60 seconds in Africa, a minute passes.

    :return:
    """
    logger.info(f" 📑 Creating {filename} in {os.getcwd()}")
    try:
        with open(filename, "w", False, "utf-8") as file:
            file.close()
    except PermissionError as error:
        logger.critical(f" ❌ Could not create {filename}: insufficient persmissions")
        sys.exit(error.errno)

def main():
    """
    Description: Entry point for installation

    :return:
    """
    logger.info(" 🧰 Attempting to install packages")
    dependencies: dict = load_dependencies("" if os.path.split(os.path.dirname(os.getcwd()))[1].__ne__("Trakr") else "..")
    # NOTE Dependencies that were updated in the process of installation
    updated_dependencies = {}

    for dependency in dependencies:
        if not dependencies[dependency]["installed"]:
            # https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
            # NOTE Returns an open file object connected to pipe 
            os.popen("python -m pip install {dependency}=={version}".format(
                dependency=dependency,
                version=dependencies[dependency]["version"])).read()  # NOTE read suppresses output
            # Assign an "is_installed" | "installed" value.
            updated_dependencies[dependency] = {}
            updated_dependencies[dependency]["installed"] = dependencies[dependency]["installed"]
            updated_dependencies[dependency] = dependencies[dependency]

    if len(updated_dependencies.keys()):
        changed_dependencies = dependencies
        dependency_count = count_dependencies(changed_dependencies)  # NOTE when adding test cases, test both vars equal
        for index, dependency in enumerate(updated_dependencies):
            logger.info(" [{dependency_id}/{dependency_amt}] Updating dependency {dependency_name}={dependency_version}".format(
                dependency_id=str(index),
                dependency_amt=dependency_count,
                dependency_name=dependency,
                dependency_version=updated_dependencies[dependency]["version"]))

    logger.info(" 🎉 Success!")

if __name__ == "__main__":
    logger = setup_logger_object()
    handle_cli_args()
    main()
