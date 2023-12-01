"""
Listagem 8.26 – Funções como parâmetro
"""


def soma(num1, num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return num1 + num2


def subtracao(num1, num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return num1 - num2


def imprime(num1, num2, foper):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_
        foper (_type_): _description_
    """
    print(foper(num1, num2))


imprime(5, 4, soma)
imprime(10, 1, subtracao)
