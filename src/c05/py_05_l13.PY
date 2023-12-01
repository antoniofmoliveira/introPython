"""
Listagem 5.13 - Interrompendo a repetição
"""
S = 0
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    S = S + v
print(S)
