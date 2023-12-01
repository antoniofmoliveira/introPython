"""
Listagem 6.44 – Ordenação pelo método de bolhas
"""
L = [7, 4, 3, 12, 8]
FIM = 5
while FIM > 1:
    TROCOU = False
    X = 0
    while X < (FIM - 1):
        if L[X] > L[X + 1]:
            TROCOU = True
            TEMP = L[X]
            L[X] = L[X + 1]
            L[X + 1] = TEMP
        X += 1
    if not TROCOU:
        break
    FIM -= 1
for e in L:
    print(e)
