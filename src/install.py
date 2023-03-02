"""
License: see attatched snippet
Copyright (c) 2023 Joshua Rose

The installer file is necessary to install dependencies required
for this project. It can be run with or without command line arguments,
however, these are developer features. More information on this is found 
in the handle_cli_args (name may and have may changed)

If there are any bugs in this file, or any problems or issues,
pull requests are encouraged and highly appreciated.

submit a bug report: https://github.com/JoshuaDRose/Trakr/issues/new

TODO: 🪴 emoticons
TODO:    log folder
"""

import sys
# NOTE see docs.python.org/3.10/library/os.html
import os
import json

import logging
import logging.config

import util

args: set[str] = sys.argv[1:] # NOTE remove the first element on the right side
logger: None | object = None # Placeholder for logger object

def handle_cli_args():
    """
    Description: A file rarely needs change, but this
    allows developers the authority to do so in that case.

    return: ...
    """

    @staticmethod
    def reset_install():
        """
        Description: I seldom use nested functions, but this is to minimize
        complexity when reading the file. I can look at handle_cli_args
        as one function; it need not be so complex.

        return: ...
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
    dependency_file_name: str = locate_directory(
            locate_dependencies(file="package.json"))
    try:
        load_dependency_as_object(dependency_file_name)
    except FileNotFoundError:
        logger.warning(" 🔎 Could not find file - changing location")
        load_dependency_as_object(dependency_file_name)
    return dependency_file

<<<<<<< HEAD
def locate_directory(file = 'config.ini') -> str:
=======
def count_dependencies(file: dict) -> int:
>>>>>>> origin/master
    """
    Description: Counts the dependencies in file
    file: a json object loaded from a file
    
    return: <int>
    """
    dependency_amount = len(file.keys())
    return dependency_amount


def query_create_log_file():
    """
<<<<<<< HEAD
    folder, _file = os.path.split(os.path.join(os.path.split(os.path.dirname(os.getcwd()))[1], file))
    if folder.__ne__('Trakr'):
        return os.path.join('src', _file)
    return _file
=======
    Description: Queries user as to if they'd like to create
    a logfile in the case that a file is not present.

    return: ...
    """
    logger.info(""" 🔎 Could not find {file}.
   Would you like to create a log file? [n/Y] """)
    _input = input(logger.debug())
    try:
        match _input.lower():
            case "" | "yes" | "y":
                with open(file, "w") as fp: fp.close()
                logger.debug(""" ✅ Created {} in {} """.format(
                file, os.path.join(os.getcwd(), file)))
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
        
>>>>>>> origin/master

def log_change(change: str, _file="install.log", emoji: str = str()) -> bool:
    """
    :change: message of the change to be recorded
<<<<<<< HEAD
    :emoji: unicode emoji character - NF* allowed

    :return: If the function succeeded; interpreted as <true | false>
    """
    file = locate_directory(_file)
    logger.debug("🥾 Removed un-needed variable: {file_content}", file_content=_file.__repr__())
    del _file
    fp = object()
    try:
        fp = open(file, 'a')
    except FileNotFoundError:
        _input = input(logger.debug(f" 🔎 Could not find {file}. Would you like to create a log file? [n/Y] >> "))
        match _input:
            case '':
                pass

def create_file(filename):
    """
    filename <str> the name of the file... Every 60 seconds in Africa, a minute passes.

    :return:
    """
    logger.info(f" 📑 Creating {filename} in {os.getcwd()}")
    try:
        with open(filename, 'w', False, 'utf-8') as file:
            file.close()
    except PermissionError as error:
        logger.critical(f" ❌ Could not create {filename}: insufficient persmissions")
        sys.exit(error.errno)
=======
    :emoji: unicode emoji character - NF allowed

    return: <true | false>
    """
    file = locate_directory(_file)
    fp = object()
    try:
        fp = open(file, "a")
    except FileNotFoundError:
        ...
>>>>>>> origin/master

def main():
    """
    Description: Entry point for installation

    return: ...
    """
<<<<<<< HEAD

    logging.config.fileConfig(locate_directory('config.ini')
    logger: object = logging.getLogger()
    logger.info(" 🔖 Finished preparing package metadata")
=======
>>>>>>> origin/master
    logger.info(" 🧰 Attempting to install packages")
    dependencies: dict = load_dependencies("package.json")
    # NOTE Dependencies that were updated in the process of installation
    updated_dependencies = {}

    # NOTE Dependencies that were updated in the process of installation
    updated_dependencies: list[str] | list[None] = []

    for dependency in dependencies:
        if not dependencies[dependency]["installed"]:
<<<<<<< HEAD
            # https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
            # NOTE Returns an open file object connected to pipe 
            os.popen('python -m pip install {dependency}=={version}'.format(
                dependency=dependency,
                version=dependencies[dependency]["version"]))

    if len(updated_dependencies):
        changed_dependencies = dependencies
        for index, dependency in enumerate(updated_dependencies):
            logger.info("🖊️ Updating dependency #{dependency_id}".format(
                dependency_id=str(index)))
            changed_dependencies[dependency]["update"]
=======
            # NOTE Returns an open file object connected to pipe 
            os.popen("python -m pip install {dependency}=={version}".format(
                dependency=dependency,
                # NOTE read suppresses output
                version=dependencies[dependency]["version"])).read()
            # Assign an "is_installed" | "installed" value.
            updated_dependencies[dependency] = {}
            updated_dependencies[dependency]["installed"] = \
                    dependencies[dependency]["installed"]
            updated_dependencies[dependency] = dependencies[dependency]

    if len(updated_dependencies.keys()):
        changed_dependencies = dependencies
        # NOTE when adding test cases, test both vars equal
        dependency_count = count_dependencies(changed_dependencies)
        for index, dependency in enumerate(updated_dependencies):
            logger.info(""" [{dependency_id}/{dependency_amt}] Updating
dependency {dependency_name}={dependency_version}""".format(
                dependency_id=str(index),
                dependency_amt=dependency_count,
                dependency_name=dependency,
                dependency_version=\
                        updated_dependencies[dependency]["version"]))
>>>>>>> origin/master

    logger.info(" 🎉 Success!")

if __name__ == "__main__":
    logger = setup_logger_object()
    handle_cli_args()
    main()

# * NF = nerd font
