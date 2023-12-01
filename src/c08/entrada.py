"""
Listagem 8.34 – Módulo entrada (entrada.py)
"""


def valida_inteiro(mensagem, minimo, maximo):
    """_summary_

    Args:
        mensagem (_type_): _description_
        minimo (_type_): _description_
        maximo (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            # else:
            print(f"Digite um valor entre {minimo:d} e {maximo:d}")
        except ValueError:
            print("Você deve digitar um número inteiro")
