"""
Exercício 6.10 Modifique o programa do exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v
foram encontrados.
"""
L = [15, 7, 27, 39, 32, 6, 4, 99]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite outro valor a procurar:"))
achados = []
posicoes = []
X = 0
while X < len(L):
    if L[X] in (p, v):
        achados.append(L[X])
        posicoes.append(X)
    X += 1
if len(achados) == 0:
    print(f"{p:d} e {v:d} não encontrados.")
elif len(achados) == 1:
    print(f"Apenas {achados[0]:d} foi achado na posição {posicoes[0]:d}.")
else:
    print(f"{achados[0]:d}  foi achado primeiro na posição {posicoes[0]:d}.")
    print(f"{achados[1]:d}  foi achado depois na posição {posicoes[1]:d}.")
