"""
Listagem 8.9 – Cálculo do fatorial
"""


def fatorial(numero):
    """fatorial de um número

    Args:
        numero (int): número do qual se quer o fatorial

    Returns:
        int: fatorial do argumento
    """
    fat = 1
    while numero > 1:
        fat *= numero
        numero -= 1
    return fat

# não é boa prática alterar o valor de argumento passado a uma função
