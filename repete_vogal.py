#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

'''
Repete vogais

Recebe uma palavra e imprime a palavra com as vogais repetidas.

'''
import os
import sys
import logging

log = logging.getLogger("vogais")

vogais = ["a", "e", "i", "o", "u"]


palavra = input("Digite uma palavra: ").strip()
novaPalavra = str()

print(palavra)


for letra in palavra:
    if letra in vogais:
        novaPalavra = novaPalavra + letra + letra
    else:
        novaPalavra = novaPalavra + letra


print("======================================")
print(novaPalavra)



# aula
words = []
while True:
    word = input("Digite uma palavra: ").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep="\n")
