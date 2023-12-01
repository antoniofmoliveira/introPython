"""
Listagem 8.27 – Configuração de funções com funções
"""


def imprime_lista(plista, fimpressao, fcondicao):
    """_summary_

    Args:
        lista (_type_): _description_
        fimpressao (_type_): _description_
        fcondicao (_type_): _description_
    """
    for elemento in plista:
        if fcondicao(elemento):
            fimpressao(elemento)


def imprime_elemento(elemento):
    """_summary_

    Args:
        elemento (_type_): _description_
    """
    print(f"Valor: {elemento:d}")


def eh_par(numero):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return numero % 2 == 0


def eh_impar(numero):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return not eh_par(numero)


lista = [1, 7, 9, 2, 11, 0]
imprime_lista(lista, imprime_elemento, eh_par)
imprime_lista(lista, imprime_elemento, eh_impar)
