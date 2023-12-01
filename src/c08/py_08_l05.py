"""
Listagem 8.5 – Pesquisa em uma lista
"""


def pesquise(lista, valor):
    """Pesquisa em uma lista

    Args:
        lista (genérico): lista de valores
        valor (genérico): valor a ser procurado. deve ser do mesmo tipo dos
        elementos de lista.

    Returns:
        int: índice do elemento se encontrado
        None: se valor não encontrado na lista
    """
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
