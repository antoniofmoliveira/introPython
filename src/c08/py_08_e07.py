"""
Exercício 8.7 Defina uma função recursiva que calcule o maior divisor comum
(M.D.C.) entre dois números a e b, onde a > b.
"""


def mdc(num1, num2):
    """calcula MDC de dois números

    Args:
        num1 (numerico): primeiro argumento, tem que ser maior que o segundo
        argumento
        num2 (numerico): segundo argumento

    Returns:
        numerico: o MDC
    """
    if (num1 % num2) == 0:
        return num2
    return mdc(num2, (num1 % num2))


print(mdc(48, 30))
print(mdc(90, 36))
