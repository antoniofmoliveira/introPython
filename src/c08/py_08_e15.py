"""
Exercício 8.15 Utilizando a função type, escreva uma função recursiva que
imprima os elementos de uma lista. Cada elemento deve ser impresso
separadamente, um por linha. Considere o caso de listas dentro de listas,
como L=[1, [2,3,4,[5,6,7]]]. A cada nível, imprima a lista mais à direita,
como fazemos ao indentar blocos em Python. Dica: envie o nível atual como
parâmetro e utilize-o para calcular a quantidade de espaços em branco à
esquerda de cada elemento.
"""


def imp_lista(nivel, lista):
    """imprime lista identanto conforme nivel de aninhamento de lista

    Args:
        nivel (_type_): nivel de identação inicial
        lista (_type_): a lista a ser impressa
    """
    for elemento in lista:
        if isinstance(elemento, list):
            imp_lista(nivel + 1, elemento)
        else:
            print(nivel * " ", end="")
            print(elemento)


LISTA = L = [1, [2, 3, 4, [5, 6, 7]]]
imp_lista(1, LISTA)
