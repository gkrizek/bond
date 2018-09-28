import click
import json
import subprocess
from sys import exit


def get_unbonded_atom(address):
    try:
        process = subprocess.check_output("gaiacli account %s" % (address), shell=True, stderr=subprocess.STDOUT)
        return {
            "success": True,
            "output": process
        }
    except subprocess.CalledProcessError as err:
        return {
            "success": False,
            "output": err.output
        }


def bond_steak(address_validator, name, steak, chain_id):
    try:
        process = subprocess.check_output("gaiacli stake delegate --amount=%s --address-validator=%s --name=%s --chain-id=%s" % (steak, address_validator, name, chain_id), shell=True, stderr=subprocess.STDOUT)
        return {
            "success": True,
            "output": process
        }
    except subprocess.CalledProcessError as err:
        return {
            "success": False,
            "output": err.output
        }


def check_bonder(address, address_validator, chain_id, name, verbose):
    if verbose:
        click.echo("Checking for address %s" % (address))
    account = get_unbonded_atom(address)
    if not account['success']:
        click.secho("Error getting account information:", fg="red", bold=True)
        print(account)
        exit(1)
    account = json.loads(account['output'])
    coin_list = account['value']['coins']
    for c in coin_list:
        if c['denom'] == 'steak':
            steak = c['amount']

    if verbose:
        click.echo("Found %s steak" %(steak))

    if steak > 0:
        bond = bond_steak(name, address, steak, chain_id)
        if not bond['success']:
            click.secho("Error bonding steak:", fg="red", bold=True)
            print(bond)
            exit(1)
        click.echo("Successfully bonded %s steak:" % (steak))
        print(bond)
    return
