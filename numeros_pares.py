#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

'''
Imprimir numeros de 1 a 200
'''

for i in range(1, 201):
    print(i if i % 2 == 0 else '')


# aula
for i in range(1, 201):
    if i % 2 != 0:
        continue
    print(i)