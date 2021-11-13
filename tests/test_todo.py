# tests/test_rptodo.py

from typer.testing import CliRunner
from todoapp import __app_name__, __version__, cli

runner = CliRunner()