"""
Listagem 8.28 – Empacotamento de parâmetros em uma lista
"""


def soma(num1, num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_
    """
    print(num1 + num2)


lista = [2, 3]
print(soma(*lista))
