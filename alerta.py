#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

'''
Alarme de temperatura

Saber qual temperatura atual e o indidice de umidade, devera ser informado ao usurio a msg conformas as condicoes abaixo:

temp > 45: Alerta!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: Alerta!!! Perigo calor umido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0: Alerta!!! Perigo frio extremo

'''
import os
import sys
import logging

log = logging.getLogger("alerta")

try:
    temperatura = float(input("Qual temperatura atual? ").strip())
except ValueError:
    log.error("Temperatura invalida")
    sys.exit(1)

try:
    umidade = float(input("Qual o indice de umidade? ").strip())
except ValueError:
    log.error("Umidade invalida")
    sys.exit(1)

print(f"Temperatura: {temperatura}")
print(f"Umidade: {umidade}")

print("======================================")

if temperatura > 45:
    print("Alerta!!! Perigo calor extremo")

elif temperatura * 3 >= umidade:
    print("Alerta!!! Perigo calor umido")

elif temperatura >= 10 and temperatura <= 30:
    print("Normal")

elif temperatura < 0:
    print("Frio")
