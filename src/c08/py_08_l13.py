"""
Listagem 8.14 – Função recursiva de Fibonacci
"""


def fibonacci(numero):
    """fibonacci na posição número

    Args:
        numero (int): posição da sequência do qual se quer o fibonacci

    Returns:
        int: fibonacci na posição número
    """
    if numero <= 1:
        return numero
    # else:
    return fibonacci(numero - 1) + fibonacci(numero - 2)


print(fibonacci(10))
