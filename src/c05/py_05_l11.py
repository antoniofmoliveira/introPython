"""
Listagem 5.11 - Soma de 10 números
"""
N = 1
SOMA = 0
while N <= 10:
    x = int(input(f"Digite o {N:d}° número: "))
    SOMA = SOMA + x
    N = N + 1
print(f"Soma: {SOMA:d}.")
