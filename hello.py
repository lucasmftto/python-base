#!/usr/bin/env python3

# Cometario Python
"""

Utiliznado variavel de ambiente

Como usar:
tenha a variavel LANG configurada

    export=pt_BR

"""
__version__ = "0.0.2    "
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os

current_languge = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo",
    "es_SP": "Holam Mundo!",
    "fr_FR": "Bonjour, Monde!",
}


print(msg[current_languge])

