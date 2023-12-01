"""
Listagem 8.7 – Soma e cálculo da média de uma lista
"""


def media(lista):
    """média dos elementos de uma lista

    Args:
        lista (numérico): list com elementos numéricos

    Returns:
        numérico: a soma dos elementos da lista dividido pelo tamanho da lista
    """
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)
