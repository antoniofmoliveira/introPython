"""
Listagem 7.12 – Pesquisa de todas as ocorrências
"""
S = "um tigre, dois tigres, três tigres"
P = 0
while P > -1:
    P = S.find("tigre", P)
    if P >= 0:
        print(f"Posição: {P:d}")
        P += 1
