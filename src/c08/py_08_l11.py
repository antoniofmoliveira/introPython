"""
Listagem 8.11 – Função recursiva do fatorial
"""


def fatorial(numero):
    """fatorial de um número

    Args:
        numero (int): número do qual se quer o fatorial

    Returns:
        int: fatorial do argumento
    """
    if numero in (0, 1):
        return 1
    # else:
    return numero * fatorial(numero - 1)
