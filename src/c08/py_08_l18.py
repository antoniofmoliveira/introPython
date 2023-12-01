"""
Listagem 8.18 – Função para imprimir uma barra na tela com parâmetros opcionais
"""


def barra(qtde_caracteres=40, caractere="*"):
    """imprime uma barra de caracteres na tela

    Args:
        qtde_caracteres (int, optional): quantidade de caracteres.
        Defaults to 40.
        caractere (str, optional): caracter a ser impresso. Defaults to "*".
    """
    print(caractere * qtde_caracteres)


# Listagem 8.19 – Passagem de parâmetros opcionais

barra(10)
barra(10, "-")
