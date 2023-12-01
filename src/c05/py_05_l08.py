"""
Listagem 5.8 - Impressão de números pares de 0 até um número digitado pelo
usuário, sem if
"""
fim = int(input("Digite o último número a imprimir:"))
X = 0
while X <= fim:
    print(X)
    X = X + 2
