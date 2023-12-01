"""
Exercício 8.2 Escreva uma função que receba dois números e retorne True se o
primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8,4) == True
múltiplo(7,3) == False
múltiplo(5,5) == True
"""


def multiplo(num1, num2):
    """retorna true se o primeiro argumento for múltiplo do segundo argumento

    Args:
        num1 (numérico): primeiro argumento
        num2 (numérico): segundo argumento

    Returns:
        boolean: True se primeiro argumetno for múltimo do segunddo argumento
    """
    return num1 % num2 == 0


print(multiplo(8, 4) is True)
print(multiplo(7, 3) is False)
print(multiplo(5, 5) is True)
