"""
Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas
p, leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.
"""
L = [15, 7, 27, 39, 32, 6, 4, 99]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite outro valor a procurar:"))
achados = []
X = 0
while X < len(L):
    if L[X] in (p, v):
        achados.append(L[X])
    X += 1
if len(achados) == 0:
    print(f"{p:d} e {v:d} não encontrados.")
elif len(achados) == 1:
    print(f"Apenas {achados[0]:d} foi achado.")
else:
    print(f"{achados[0]:d}  foi achado primeiro.")
    print(f"{achados[1]:d}  foi achado depois.")
