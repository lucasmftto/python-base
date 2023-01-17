#!/usr/bin/env python3

# Cometario Python
"""

Utiliznado variavel de ambiente

Como usar:
tenha a variavel LANG configurada

    export=pt_BR

"""
__version__ = "0.0.1"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os

current_languge = os.getenv("LANG", "en_US")[:5]
msg = "Hello, Word!"

if current_languge == "pt_BR":
    msg = "Olá, Mundo!"
elif current_languge == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)

