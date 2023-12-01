"""
Exercício 8.10 Reescreva a função para cálculo da sequência de Fibonacci, sem
utilizar recursão.
"""


def fibonnacci2(numero):
    """fibonacci na posição número

    Args:
        numero (int): posição da sequência do qual se quer o fibonacci

    Returns:
        int: fibonacci na posição número
    """
    acc1 = 1
    acc2 = 1
    acc = 0
    for num in range(numero):
        if num <= 1:
            acc += 1
        else:
            acc = acc1 + acc2
            acc1 = acc2
            acc2 = acc
    return acc


print(fibonnacci2(9))
