"""
Exercício 6.1 Modifique o programa da listagem 6.6 para ler 7 notas em vez
de 5.
"""
notas = [0, 0, 0, 0, 0, 0, 0]
SOMA = 0
X = 0
while X < 7:
    notas[X] = float(input(f"Nota {X:d}: "))
    SOMA += notas[X]
    X += 1
X = 0
while X < 7:
    print(f"Nota {X:d}: {notas[X]:6.2f}.")
    X += 1
print(f"Média: {(SOMA / X):5.2f}.")
