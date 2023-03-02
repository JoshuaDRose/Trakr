"""
TODO: 🪴 emoticons
TODO:    log folder
"""
import sys
# NOTE see docs.python.org/3.10/library/os.html
import os
import json

import logging
import logging.config

def load_dependencies(root) -> dict:
    """
    Description: Load file object from parent directory.

    :return: dict
    """
    dependency_file: dict = json.load(open(os.path.join(root, 'package.json'), 'r'))
    return dependency_file

def locate_directory(file = 'config.ini') -> str:
    """
    Description: Locate file through determining the root folder

    :return: str
    """
    folder, _file = os.path.split(os.path.join(os.path.split(os.path.dirname(os.getcwd()))[1], file))
    if folder.__ne__('Trakr'):
        return os.path.join('src', _file)
    return _file

def log_change(change: str, _file="install.log", emoji: str = str()) -> bool:
    """
    :change: message of the change to be recorded
    :emoji: unicode emoji character - NF* allowed

    :return: If the function succeeded; interpreted as <true | false>
    """
    file = locate_directory(_file)
    # logger.debug("🥾 Removed un-needed variable: {file_content}", file_content=_file.__repr__())
    fp = object()
    try:
        fp = open(file, 'a')
    except FileNotFoundError:
        _input = input(logger.debug(f" 🔎 Could not find {file}. Would you like to create a log file? [n/Y] >> "))
        try:
            match _input.lower():
                case '' | 'yes' | 'y':
                    with open(file, 'w') as fp: fp.close()
                    logger.debug(f" ✅ Created {file} in {os.path.join(os.getcwd(), file)} ")
                    log_change(change, _file, emoji)
                    return
                case 'n':
                    logger.debug("   Ignoring log file creation.")
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
        with open(filename, 'w', False, 'utf-8') as file:
            file.close()
    except PermissionError as error:
        logger.critical(f" ❌ Could not create {filename}: insufficient persmissions")
        sys.exit(error.errno)

def main():
    """
    Description: Entry point for installation

    :return:
    """

    logging.config.fileConfig(locate_directory('config.ini'))
    logger: object = logging.getLogger()
    logger.info(" 🔖 Finished preparing package metadata")
    logger.info(" 🧰 Attempting to install packages")
    dependencies: dict = load_dependencies('' if os.path.split(os.path.dirname(os.getcwd()))[1].__ne__('Trakr') else '..')

    # NOTE Dependencies that were updated in the process of installation
    updated_dependencies: list[str] | list[None] = []

    for dependency in dependencies:
        if not dependencies[dependency]["installed"]:
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

    logger.info(" 🎉 Success!")

if __name__ == "__main__":
    main()

# * NF = nerd font
