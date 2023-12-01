"""
Listagem 8.10 – Outra forma de calcular o fatorial
"""


def fatorial(numero):
    """fatorial de um número

    Args:
        numero (int): número do qual se quer o fatorial

    Returns:
        int: fatorial do argumento
    """
    fat = 1
    contador = 1
    while contador <= numero:
        fat *= contador
        contador += 1
    return fat
