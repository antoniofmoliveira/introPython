"""
Listagem 8.29 – Outro exemplo de empacotamento de parâmetros em uma lista
"""


def barra(qtde=10, caracter="*"):
    """_summary_

    Args:
        qtde (int, optional): _description_. Defaults to 10.
        caracter (str, optional): _description_. Defaults to "*".
    """
    print(caracter * qtde)


lista = [[5, "-"], [10, "*"], [5], [6, "."]]
for elemento in lista:
    barra(*elemento)
