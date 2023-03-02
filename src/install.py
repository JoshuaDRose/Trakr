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
    logger.debug("🥾 Removed un-needed variable: {file_content}", file_content=_file.__repr__())
    del _file
    with open(file)

def main():
    """
    Description: Entry point for installation

    :return:
    """

    logging.config.fileConfig(locate_directory('config.ini')
    logger: object = logging.getLogger()
    logger.info(" 🔖 Finished preparing package metadata")
    logger.info(" 🧰 Attempting to install packages")
    dependencies: dict = load_dependencies('' if os.path.split(os.path.dirname(os.getcwd()))[1].__ne__('Trakr') else '..')

    # NOTE Dependencies that were updated in the process of installation
    updated_dependencies: list[str] | list[None] = []

    for dependency in dependencies:
        if not dependencies[dependency]["installed"]:
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
