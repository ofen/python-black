#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: thepoy
# @Email: thepoy@163.com
# @File Name: constants.py
# @Created: 2021-03-27 09:55:27
# @Modified: 2021-06-11 23:45:03

PACKAGE_NAME: str = "python-black"
INSTALLED_PACKAGE_NAME: str = f"{PACKAGE_NAME}.sublime-package"
SETTINGS_FILE_NAME: str = f"{PACKAGE_NAME}.sublime-settings"

WORKER_TIMEOUT: int = 0
WORKER_START_TIMEOUT: int = 100
STATUS_MESSAGE_TIMEOUT: int = 3000

COMMAND: str = "black"
CODE: str = "-c"
CONFIG: str = "--config"

TIMEOUT: int = 0
FORMAT_TIMEOUT: int = 100

CONFIGURATION_FILENAME: str = "pyproject.toml"
CONFIGURATION_CONTENTS: str = """[tool.black]
line-length = 120
target-version = ['py38']
include = '\\.pyi?\\$'
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/foo.py  # exclude a file named foo.py in the root of the project (in addition to the defaults)
'''"""
