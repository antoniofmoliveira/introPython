"""
Listagem 6.5 - Cálculo da média
"""
notas = [6, 7, 5, 8, 9]
SOMA = 0
X = 0
while X < 5:
    SOMA += notas[X]
    X += 1
print(f"Média: {(SOMA/X):5.2f}.")
