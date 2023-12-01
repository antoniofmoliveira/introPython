"""
Listagem 6.23 – Pesquisa sequencial
"""
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
ACHOU = False
X = 0
while X < len(L):
    if L[X] == p:
        ACHOU = True
        break
    X += 1
if ACHOU:
    print(f"{p:d} achado na posição {X:d}.")
else:
    print(f"{p:d} não encontrado.")
