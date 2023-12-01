"""
Listagem 6.15 - Adição de elementos à lista
"""

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for X in L:
    print(X)
