#!/usr/bin/env python

from mylib.logistics import total_distance, CITIES
import click


@click.group()
def cli():
    """Tool for calculating total distance between a list of cities"""


@cli.command("total")
def total():
    """Calculate the total distance between a list of cities"""
    print(total_distance(CITIES))


if __name__ == '__main__':
    cli()