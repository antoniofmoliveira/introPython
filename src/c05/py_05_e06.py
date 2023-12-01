"""
Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo
formato de uma tabuada: 2x1 = 2, 2x2=4, ...
"""
n = int(input("Tabuada de: "))
X = 1
while X <= 10:
    print(f"{n:2d} x {X:2d} = {(n * X):3d}")
    X = X + 1
