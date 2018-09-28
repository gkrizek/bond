#!/usr/bin/env python
import click
from time import sleep
from sys import exit
from .check import check_atom
from .__init__ import __version__

# Constants
CHECK_INTERVAL = 10


@click.group()
def bonder():
    """
    \b
    BONDER TEXT

    Bonder - Atom Auto-Bonding for a Cosmos Validator
    """


@bonder.command('start', short_help="start bonder")
@click.option('--verbose', default=False, is_flag=True, help="add additional logging")
def start(verbose):
    while True:
        check_bonder(verbose)
        sleep(CHECK_INTERVAL)


@bonder.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Bonder v%s" % (__version__))
    click.echo("")
