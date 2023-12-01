"""
Listagem 8.45 – Navegando listas a partir do tipo de seus elementos
"""
# import types

LISTA = ["a", ["b", "c", "d"], "e"]
for elemento in LISTA:
    # if type(elemento) == str:
    if isinstance(elemento, str):
        print(elemento)
    else:
        print("Lista:")
        for subelem in elemento:
            print(subelem)
