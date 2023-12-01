"""
Exercício 8.1 Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7
"""


def maximo(num1, num2):
    """retorna o maior de 2 argumento numéricos num1 e num2

    Args:
        num1 (numérico): primeiro argumento
        num2 (numérico): segundo argumento

    Returns:
        numérico: o primeiro argumento se este for maior que o segundo,
        o segundo argumento casa contrário
    """
    if num1 >= num2:
        return num1
    # else:
    return num2


print(maximo(5, 6) == 6)
print(maximo(2, 1) == 2)
print(maximo(7, 7) == 7)
