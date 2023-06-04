#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas Favaretto"
__license__ = "Unlicense"


names = ["Lucas", "Favaretto", "Python", "Bruno", "Campinas"]

# TODO: Usar lambda




print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")