#!/usr/bin/env python3

# Cometario Python
"""

Utiliznado variavel de ambiente

Como usar:
tenha a variavel LANG configurada

    export=pt_BR

"""
__version__ = "0.0.3"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error("Erro ao realizar split: %s ", {str(e)})
        log.info("You need to use `=`")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_languge = arguments["lang"]
if current_languge is None:
    current_languge = os.getenv("LANG")
    if current_languge is None:
        current_languge = input(
            "Choose a language: "
        )

current_languge = current_languge[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo",
    "es_SP": "Holam Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

try:
    message = msg[current_languge]
except KeyError as e:
    print(f"[ERROR]: {str(e)}")
    print(f"Language is Invalide, choose from: {list(msg.keys()) }")
    sys.exit(1)


# message = msg.get(current_languge, msg["pt_BR"])

print(message * int(arguments["count"]))

