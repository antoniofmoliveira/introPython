"""
Exercício 7.6 Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1a string: AATTCGAA
2a string: TG
3a string: AC
Resultado: AAAACCAA
"""

termo1 = input("Digite primeiro termo: ")
termo2 = input("Digite segundo termo: ")
termo3 = input("Digite terceiro termo: ")
lista = list(termo1)
comum = []
X = 0
while X < len(termo2):
    Y = 0
    while Y < len(lista):
        if termo2[X] == lista[Y]:
            lista[Y] = termo3[X]
        Y += 1
    X += 1
print("".join(lista))
