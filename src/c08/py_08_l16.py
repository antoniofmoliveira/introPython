"""
Listagem 8.16 – Validação de inteiro usando função
"""


def faixa_int(pergunta, minimo, maximo):
    """Validação de inteiro usando função

    Args:
        pergunta (int): mensagem para exbir solicitando entrada de dados
        minimo (int): valor minimo aceito
        maximo (int): valor máximo aceito

    Returns:
        int: o valor informado
    """
    while True:
        valor = int(input(pergunta))
        if valor < minimo or valor > maximo:
            print("Valor inválido." +
                  f" Digite um valor entre {minimo:d} e {maximo:d}")
        else:
            return valor
