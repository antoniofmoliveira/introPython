"""
Exercício 6.12 Altere o programa da listagem 6.33 de forma a imprimir o menor
elemento da lista.
"""
L = [1, 7, 2, 4]
MINIMO = L[0]
for e in L:
    if e < MINIMO:
        MINIMO = e
print(MINIMO)
