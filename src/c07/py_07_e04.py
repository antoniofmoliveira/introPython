"""
Exercício 7.4 Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""
termo = input("Digite o termo: ")
contagem = {}
for e in termo:
    if e in contagem:
        contagem[e] += 1
    else:
        contagem[e] = 1
for k, v in contagem.items():
    print(f"{k}: {v:d}x")
