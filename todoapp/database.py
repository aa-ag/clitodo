import configparser
from pathlib import Path

from todoapp import DB_WRITE_ERROR, SUCCESS


DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

