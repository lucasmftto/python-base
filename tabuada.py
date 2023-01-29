#!/usr/bin/env python

"""Imprime tabuada do 1 ao 10"""

__version__ = "0.1.1"
__author__ = "Lucas Favaretto"

template_base = """
---Tabuada do {operador}---

{bloco}

#######################
"""

#base = [1, 2, 3, 5, 6, 7, 8, 9, 10]
base = list(range(1, 11))


for n1 in base:
    bloco = "{:^2}".format("")
    for n2 in base:
        resultado = n1 * n2
        bloco += "{:^16}".format(f"{n1} X {n2} = {resultado}\n")
    print(template_base.format(bloco=bloco, operador=n1))
    
