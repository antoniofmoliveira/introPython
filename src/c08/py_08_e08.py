"""
Exercício 8.8 Usando a função mdc definida no exercício anterior, defina uma
função para calcular o menor múltiplo comum (M.M.C.) entre dois números.
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


def mmc(num1, num2):
    """calcula MMC de dois números

    Args:
        num1 (numerico): primeiro argumento, tem que ser maior que o segundo
        argumento
        num2 (numerico): segundo argumento

    Returns:
        numerico: o MMC
    """
    return abs(num1 * num2) / mdc(num1, num2)


print(mmc(6, 4))
