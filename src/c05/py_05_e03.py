"""
Exercício 5.3 Faça um programa para escrever a contagem regressiva do
lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo!
na tela.
"""
X = 10
while X >= 0:
    if X != 0:
        print(f"{X}, ", end="")
    else:
        print(f"{X} ", end="")
    X = X - 1
print("e Fogo!")
