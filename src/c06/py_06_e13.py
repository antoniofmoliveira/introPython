"""
Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na
lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor
e a maior temperatura, assim como a temperatura média.
"""
T = [-10, -8, 0, 1, 2, 5, -2, -4]
MINIMA = T[0]
MAXIMA = T[0]
for e in T:
    if e < MINIMA:
        MINIMA = e
    elif e > MAXIMA:
        MAXIMA = e
print(f"Mínima de {MINIMA:d}° e máxima de {MAXIMA:d}°.")
