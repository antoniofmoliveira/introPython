"""
Listagem 6.34 - Cópia de elementos para outras listas
"""
VALORES = [9, 8, 7, 12, 0, 13, 21]
PARES = []
IMPARES = []
for e in VALORES:
    if e % 2 == 0:
        PARES.append(e)
    else:
        IMPARES.append(e)
print("Pares: ", PARES)
print("Impares: ", IMPARES)
