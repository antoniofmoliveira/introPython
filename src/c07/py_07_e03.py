"""
Exercício 7.3 Escreva um programa que leia duas strings e gere uma terceira
apenas com os caracteres que aparecem em uma delas.
1a string: CTA
2a string: ABC
3a string: BT
A ordem dos caracteres da terceira string não é importante.
"""
termo1 = input("Digite primeiro termo: ")
termo2 = input("Digite segundo termo: ")
comum = []
for e in termo1:
    if termo2.find(e) < 0:
        comum.append(e)
for e in termo2:
    if termo1.find(e) < 0:
        comum.append(e)
print("".join(comum))
