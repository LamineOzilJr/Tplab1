import math


def calc_distance(point1, point2):
    # Extraits les coordonnees des points
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calcul de la distance
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return distance


point1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
point2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]


# Definition de ma fonction
def my_map(func, list1, list2):
    return [func(elem1, elem2) for elem1, elem2 in zip(list1, list2)]


# Calcul des distances entre chaque paire de points
distances = my_map(calc_distance, point1, point2)

print(distances)
