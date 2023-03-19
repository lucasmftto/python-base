#!/usr/bin/env python3
"""Bloco de Notas 
$ notes.py new "Minha Nota"

tag: tech
text: 
Anotacao gera sobre tech


$ notes.py reaf tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")

if arguments[0] not in cmds:
    print("Invalid args")
    sys.exit(1)


if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")    
            print(f"Text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    title = arguments[1]
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
