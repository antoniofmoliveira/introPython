"""
Listagem 8.31 – Função imprime_maior com número indeterminado de parâmetros
"""


def imprime_maior(mensagem, *numeros):
    """_summary_

    Args:
        mensagem (_type_): _description_
    """
    maior = None
    for elemento in numeros:
        if maior is None or maior < elemento:
            maior = elemento
    print(mensagem, maior)


imprime_maior("Maior:", 5, 4, 3, 1)
imprime_maior("Max:", *[1, 7, 9])
