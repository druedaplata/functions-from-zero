#!/usr/bin/env python

from mylib.logistics import (
    cities_list,
    distance_between_two_points,
    get_coordinates,
    travel_time,
)
import click


@click.group()
def cli():
    """Logistics command-line"""


@cli.command("cities")
def cities():
    """
    List cities

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
    """
    Calculate distance between two cities

    Example:
    ./logisticsCLI.py distance "New York" "Los Angeles"
    """
    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(
            str(
                distance_between_two_points(
                    get_coordinates(city1), get_coordinates(city2)
                )
            ),
            fg="blue",
        )
    )


@cli.command("travel")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=60, help="Speed in miles per hour")
def travel(city1, city2, speed):
    """
    Estimate travel time between two cities by car

    Example:
    ./logisticsCLI.py travel "New York" "Los Angeles"
    """
    click.echo(click.style("Travel time between two cities", fg="green"))
    click.echo(click.style(f"{travel_time(city1, city2, speed)} hours", fg="blue"))


if __name__ == "__main__":
    cli()
