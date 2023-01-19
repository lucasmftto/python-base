#!/usr/bin/env python

"""Imprime tabuada do 1 ao 10"""

__version__ = "0.1.0"
__author__ = "Lucas Favaretto"

#base = [1, 2, 3, 5, 6, 7, 8, 9, 10]
base = list(range(1, 11))


for numero in base:
    print("Tabuada do:", numero)
    for outro_numero in base:
        print(numero * outro_numero)
    print("-------------------")
    
