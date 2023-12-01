"""
Listagem 8.12 – Função modificada para facilitar o rastreamento
"""


def fatorial(numero):
    """fatorial de um número

    Args:
        numero (int): número do qual se quer o fatorial

    Returns:
        int: fatorial do argumento
    """
    print(f"Calculando o fatorial de {numero:d}")
    if numero in (0, 1):
        print(f"Fatorial de {numero:d} = 1")
        return 1
    # else:
    fat = numero * fatorial(numero - 1)
    print(f" fatorial de {numero:d} = {fat:d}")
    return fat


fatorial(4)
