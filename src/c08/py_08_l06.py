"""
Listagem 8.6 – Cálculo da média de uma lista
"""


def soma(lista):
    """soma os elementos de uma lista

    Args:
        lista (numérico): lista com elementos numéricos

    Returns:
        numérico: valor da soma dos elementos da lista
    """
    total = 0
    for valor in lista:
        total += valor
    return total


def media(lista):
    """média dos elementos de uma lista

    Args:
        lista (numérico): list com elementos numéricos

    Returns:
        numérico: a soma dos elementos da lista dividido pelo tamanho da lista
    """
    return soma(lista) / len(lista)
