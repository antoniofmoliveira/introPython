"""
Exercício 7.2 Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1a string: AAACTBF
2a string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas
as letras comuns a ambas.
"""
termo1 = input("Digite primeiro termo: ")
termo2 = input("Digite segundo termo: ")
comum = []
for e in termo1:
    if termo2.find(e) >= 0:
        comum.append(e)
print("".join(comum))
