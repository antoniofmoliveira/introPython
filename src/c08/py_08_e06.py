"""
Listagem 8.8 – Como não escrever uma função
Exercício 8.6 Reescreva o programa da listagem 8.8 de forma a utilizar for
em vez de while.
"""


def soma(lista):
    """soma valores de listas com 5 elementos"""
    total = 0
    for indice in range(5):
        total += lista[indice]
    return total


L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))

# a função só soma os primeiros 5 elemento de uma lista
