"""
Exercício 7.5 Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1a string: AATTGGAA
2a string: TG
3a string: AAAA
"""
termo1 = input("Digite primeiro termo: ")
termo2 = input("Digite segundo termo: ")
nao_comum = []
for e in termo1:
    if termo2.find(e) < 0:
        nao_comum.append(e)
print("".join(nao_comum))
