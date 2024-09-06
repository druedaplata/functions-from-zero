from mylib.logistics import CITIES, distance_between_two_points, cities_list


def test_distance_between_two_points():
    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 3944.422231489921


def test_print_cities():
    """"""
    assert "Chicago" in cities_list()
