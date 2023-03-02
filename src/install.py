"""
TODO: 🪴 emoticons
"""
import sys
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

def locate_logger_config() -> str:
    """
    Description: Locate file through determining the root folder

    :return: str
    """
    folder, file = os.path.split(os.path.join(os.path.split(os.path.dirname(os.getcwd()))[1], 'config.ini'))
    if folder.__ne__('Trakr'):
        return os.path.join('src', file)
    return file

def main():
    """
    Description: Entry point for installation

    :return:
    """

    logging.config.fileConfig(locate_logger_config())
    logger: object = logging.getLogger()
    logger.info(" 🔖 Finished preparing package metadata")
    logger.info(" 🧰 Attempting to install packages")
    dependencies: dict = load_dependencies('' if os.path.split(os.path.dirname(os.getcwd()))[1].__ne__('Trakr') else '..')

    for dependency in dependencies:
        if not dependencies[dependency]["installed"]:
            os.system('python -m pip install {dependency}=={version}'.format(
            dependency=dependency,
            version=dependencies[dependency]["version"]))

if __name__ == "__main__":
    main()
