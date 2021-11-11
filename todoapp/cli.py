"""This module provides the RP To-Do CLI."""
# rptodo/cli.py

from typing import Optional
import typer
from todo import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
