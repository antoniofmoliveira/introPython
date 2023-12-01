"""
Listagem 8.20 – Função soma com parâmetros obrigatórios e opcionais
"""


def soma(num1, num2, imprime=False):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_
        imprime (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    resultado = num1 + num2
    if imprime:
        print(resultado)
    return resultado


print(soma(2, 3))
print(soma(3, 4, True))
print(soma(5, 8, False))
