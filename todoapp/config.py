"""This module provides the RP To-Do config functionality."""
# rptodo/config.py

import configparser
from pathlib import Path

import typer

from todoapp import (
    DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__
)

CONFIG_DIR_PATH = Path(typer.get_app_dir())
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"