"""
Exercício 6.14 O que acontece quando a lista já está ordenada? Rastreie o
programa da listagem 6.44, mas com a lista L=[1,2,3,4,5].
"""
# L = [7, 4, 3, 12, 8]
L = [1, 2, 3, 4, 5]
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
