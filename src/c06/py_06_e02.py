"""
Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com
os elementos das duas primeiras.
"""
L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9]
L3 = L1[:]
L3.extend(L2)
print(L3)
