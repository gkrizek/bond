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
@click.option('--name', help="name of address to delegate from", metavar='<NAME>')
@click.option('--chain_id', help="gaia chain id")
@click.option('--interval', default=10, help="Number of seconds to wait in between checks")
@click.option('--verbose', default=False, is_flag=True, help="add additional logging")
def start(address, address_validator, chain_id, interval, name, verbose):
    if not address or not address_validator or not name or not chain_id:
        click.secho("Error: You must provide an address, address_validator, chain_id, and name. Please use the appropriate flags", fg="red", bold=True)
        exit(1)
    first_run = True
    while True:
        if first_run and verbose:
            click.echo("Starting Bonder...")
            click.echo("Checking every %s seconds" % (interval))
            click.echo("Address: %s" % (address))
            click.echo("Validator Address: %s" % (address_validator))
            click.echo("Name: %s" % (name))
            click.echo("Chain: %s" % (chain_id))
        check_bonder(address, address_validator, chain_id, name, verbose)
        first_run = False
        sleep(interval)



@bonder.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Bonder v%s" % (__version__))
    click.echo("")
