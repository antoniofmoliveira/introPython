"""
Listagem 6.6 - Cálculo da média com notas digitadas
"""
notas = [0, 0, 0, 0, 0]
SOMA = 0
X = 0
while X < 5:
    notas[X] = float(input(f"Nota {X:d}: "))
    SOMA += notas[X]
    X += 1
X = 0
while X < 5:
    print(f"Nota {X:d}: {notas[X]:6.2f}.")
    X += 1
print(f"Média: {(SOMA / X):5.2f}.")
