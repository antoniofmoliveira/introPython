"""
Listagem 6.31 – Impressão de índices sem usar a função enumerate
"""
L = [5, 9, 13]
X = 0
for e in L:
    print(f"[{X:d}] {e:d}.")
    X += 1
