"""
Exercício 5.14 Escreva um programa que leia números inteiros do teclado.
O programa deve ler os números até que o usuário digite 0 (zero). No final da
execução, exiba a quantidade de números digitados, assim como a soma e a média
aritmética.
"""
S = 0
Q = 0
while True:
    v = float(input("Digite um número a calcula a média ou 0 para sair: "))
    if v == 0:
        break
    S = S + v
    Q += 1
print(f"A média é {(S/Q):6,.2f}.")
