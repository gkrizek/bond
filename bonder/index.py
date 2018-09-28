#!/usr/bin/env python
import click
from time import sleep
from sys import exit
from .check import check_bonder
from .__init__ import __version__

@click.group()
def bonder():
    """
    \b
     _ )   _ \   \ |  _ \  __|  _ \ 
     _ \  (   | .  |  |  | _|     / 
    ___/ \___/ _|\_| ___/ ___| _|_\ 
                                

    Bonder - Atom Auto-Bonding for a Cosmos Validator
    """


@bonder.command('start', short_help="start bonder")
@click.option('--address', help="address to check for unbonded steak", metavar='<ADDRESS>')
@click.option('--address_validator', help="validator address to bond to", metavar='<ADDRESS>')
@click.option('--name', help="name of address to delegate from", metavar='<ADDRESS>')
@click.option('--interval', default=10, help="Number of seconds to wait in between checks")
@click.option('--verbose', default=False, is_flag=True, help="add additional logging")
def start(address, address_validator, interval, name, verbose):
    if not address or not address_validator or not name:
        click.secho("Error: You must provide an address, address_validator, and name. Please use the appropriate flags", fg="red", bold=True)
        exit(1)
    first_run = True
    while True:
        if first_run and verbose:
            click.echo("Starting Bonder...")
            click.echo("Checking every %s seconds" % (interval))
            click.echo("Address: " % (address))
            click.echo("Validator Address" % (address_validator))
            click.echo("Name" % (name))
        check_bonder(address, address_validator, name, verbose)
        first_run = False
        sleep(interval)



@bonder.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Bonder v%s" % (__version__))
    click.echo("")
