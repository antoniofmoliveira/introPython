"""
Listagem 6.33 – Verificação do maior valor
"""
L = [1, 7, 2, 4]
MAXIMO = L[0]
for e in L:
    if e > MAXIMO:
        MAXIMO = e
print(MAXIMO)
