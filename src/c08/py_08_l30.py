"""
Listagem 8.30 – Função soma com número indeterminado de parâmetros
"""


def soma(*lista_numeros):
    """_summary_

    Returns:
        _type_: _description_
    """
    subtotal = 0
    for numero in lista_numeros:
        subtotal += numero
    return subtotal


print(soma(1, 2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma(9, 10, 20, 30, 40))
