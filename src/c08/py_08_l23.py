"""
Listagem 8.23 – Função retângulo com parâmetros obrigatórios e opcionais
"""


def retangulo(largura, altura, caractere="*"):
    """_summary_

    Args:
        largura (_type_): _description_
        altura (_type_): _description_
        caractere (str, optional): _description_. Defaults to "*".
    """
    # linha = caractere * largura
    # for i in range(altura):
    #     print(linha)

    print(altura * (caractere * largura + "\n"), end="")


retangulo(3, 4)
retangulo(largura=3, altura=4)
retangulo(altura=4, largura=3)
retangulo(caractere="-", altura=4, largura=3)
