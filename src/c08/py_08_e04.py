"""
Exercício 8.4 Escreva uma função que receba a base e a altura de um triângulo e
retorne sua área (A = (base x altura)/2).
Valores esperados:
área_triângulo(6, 9) == 27
área_triângulo(5, 8) == 20
"""


def area_triangulo(base, altura):
    """calcula a áre do triângulo

    Args:
        base (numérico): valor da base
        altura (numérico): valor da altura

    Returns:
        numérico: o resultado da fórmula (base * altura) / 2
    """
    return (base * altura) / 2


print(area_triangulo(6, 9) == 27)
print(area_triangulo(5, 8) == 20)
