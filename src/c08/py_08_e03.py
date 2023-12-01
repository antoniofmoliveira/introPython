"""
Exercício 8.3 Escreva uma função que receba o lado (l) de um quadrado e retorne
sua área (A = lado²).
Valores esperados:
área_quadrado(4) == 16
área_quadrado(9) == 81
"""


def area_quadrado(lado):
    """retorna a área do quadrado

    Args:
        lado (numérico): tamanho do lado do quadrado

    Returns:
        numérico: lado levado ao quadrado
    """
    return lado**2


print(area_quadrado(4) == 16)
print(area_quadrado(9) == 81)
