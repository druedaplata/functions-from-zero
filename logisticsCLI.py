#!/usr/bin/env python

from mylib.logistics import cities_list, distance_between_two_points, get_coordinates
import click


@click.group()
def cli():
    """Logistics tool"""


@cli.command("cities")
def cities():
    """List cities

    Example:
    ./logisticsCLI.py cities
    """
    click.echo(click.style("List of cities", fg="green"))
    for city in cities_list():
        click.echo(click.style(city, fg="blue"))


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """Calculate distance between two cities

    Example:
    ./logisticsCLI.py distance "New York" "Los Angeles"
    """
    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(click.style(
        f"{distance_between_two_points(get_coordinates(city1), get_coordinates(city2))}",
        fg="blue"
    )
)

if __name__ == "__main__":
    cli()
