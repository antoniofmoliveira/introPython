"""
Exercício 6.3 Faça um programa que percorra duas listas e gere uma terceira sem
elementos repetidos.
"""
L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8, 9]
L3 = L1[:]
X = 0
while X < len(L2):
    if L2[X] not in L1:
        L3.append(L2[X])
    X += 1
print(L3)
