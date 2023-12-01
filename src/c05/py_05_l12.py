"""
Listagem 5.12 - Cálculo de média com acumulador
"""
X = 1
SOMA = 0
while X <= 5:
    n = int(input(f"{X:d} Digite o número: "))
    SOMA = SOMA + n
    X = X + 1
print(f"Média: {(SOMA/5):5.2f}")
