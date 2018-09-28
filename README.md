# bonder

Atom Auto-Bonding for a Cosmos Validator

## Installation

```
$ cd /usr/local
$ git clone https://github.com/gkrizek/bonder
$ cd bonder/
$ pip install .
```

## Usage

```
$ bonder --help
Usage: bonder [OPTIONS] COMMAND [ARGS]...

   _ )   _ \   \ |  _ \  __|  _ \
   _ \  (   | .  |  |  | _|     /
  ___/ \___/ _|\_| ___/ ___| _|_\


  Bonder - Atom Auto-Bonding for a Cosmos Validator

Options:
  --help  Show this message and exit.

Commands:
  start    start bonder
  version  check agent version
```

##### start

```
$ bonder start --help
Usage: bonder start [OPTIONS]

Options:
  --address <ADDRESS>            address to check for unbonded steak
  --address_validator <ADDRESS>  validator address to bond to
  --name <NAME>                  name of address to delegate from
  --chain_id                     gaia chain id
  --interval INTEGER             Number of seconds to wait in between checks
  --verbose                      add additional logging
  --help                         Show this message and exit.
```


#### Example

```
$ bonder start \
    --address=cosmosaccaddr1j0sjgc7c0pdgqrgkcf5hdl5gn0453027h7ucsg \
    --address_validator=cosmosaccaddr10505nl7yftsme9jk2glhjhta7w0475uva87paj \
    --name=wallet1 \
    --chain_id=gaia-8001
```

## Execution

You can either background the bonder process by appending a `&` at the end of the command or setup a systemd service. [See example systemd file](./bonder.service)