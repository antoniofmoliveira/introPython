"""
Listagem 5.7 - Impressão de números pares de 0 até um número digitado pelo
usuário
"""
fim = int(input("Digite o último número a imprimir:"))
X = 0
while X <= fim:
    if X % 2 == 0:
        print(X)
    X = X + 1
