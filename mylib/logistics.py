"""

This module deals with logistics and calculates distances between two points
and the time it takes to travel between two points and other logistics related questions.
"""

from geopy import distance

CITIES = [
    ("New York", (40.7128, -74.0060)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Chicago", (41.8781, -87.6298)),
    ("Houston", (29.7604, -95.3698)),
    ("Phoenix", (33.4484, -112.0740)),
    ("Philadelphia", (39.9526, -75.1652)),
    ("San Antonio", (29.4241, -98.4936)),
    ("San Diego", (32.7157, -117.1611)),
    ("Dallas", (32.7767, -96.7970)),
    ("San Jose", (37.3382, -121.8863)),
]


def distance_between_two_points(city1, city2):
    """Calculate the distance between two cities"""
    return distance.distance(city1, city2).km


def total_distance(cities):
    """
    Calculate the total distance between a list of cities"""
    total = 0
    for i in range(len(cities) - 1):
        total += distance_between_two_points(cities[i][1], cities[i - 1][1])
    return total
