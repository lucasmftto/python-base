#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas Favaretto"
__license__ = "Unlicense"


"""Funcoes"""

def heron(a, b, c):
    """Calcula a area de um triangulo dados os lados"""
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


area_triangulo = heron(3, 4, 5)

print(area_triangulo)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")