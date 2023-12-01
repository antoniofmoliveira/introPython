"""
Listagem 6.7 - Apresentação de números
"""
numeros = [0, 0, 0, 0, 0]
X = 0
while X < 5:
    numeros[X] = int(input(f"Número {(X + 1):d}: "))
    X += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    if escolhido not in range(1, 6):
        print("Posição deve estar entre 1 e 5.")
    else:
        print(f"Você escolheu o número: {(numeros[escolhido - 1]):d}.")
