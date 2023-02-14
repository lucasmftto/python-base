#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

import pprint

produto = {
    "nome": "Caneta",
    "cores":["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "lasgura": 0.8,
    },

}

cliente = {
    "nome": "Lucas"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "qtd": 3
}

# pprint.pprint(compra)

total_compra = compra['qtd'] * compra["produto"]["preco"]
 
print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
