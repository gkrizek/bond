import click
import json
import subprocess
from sys import exit


def get_unbonded_atom(address):
    process = subprocess.Popen("gaiacli account %s" % (address), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode is 0:
        return {
            "success": True,
            "code": process.returncode,
            "output": process.stdout.read()
        }
    else:
        return {
            "success": False,
            "code": process.returncode,
            "output": process.stdout.read()
        }
    return


def bond_steak(address_validator, name, steak):
    process = subprocess.Popen("gaiacli stake delegate --amount=%s --address-validator=%s --name=%s" % (steak, address_validator, name), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode is 0:
        return {
            "success": True,
            "code": process.returncode,
            "output": process.stdout.read()
        }
    else:
        return {
            "success": False,
            "code": process.returncode,
            "output": process.stdout.read()
        }
    return


def check_bonder(address, address_validator, name, verbose):
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
        bond = bond_steak(name, address, steak)
        if not bond['success']:
            click.secho("Error bonding steak:", fg="red", bold=True)
            print(bond)
            exit(1)
        click.echo("Successfully bonded steak:")
        print(bond)



    return
