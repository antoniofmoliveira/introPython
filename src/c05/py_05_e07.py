"""
Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo
formato de uma tabuada: 2x1 = 2, 2x2=4, ...
"""
n = int(input("Tabuada de: "))
i = int(input("Início da tabuada: "))
f = int(input("Fim da tabuada: "))
X = i
while X <= f:
    print(f"{n:2d} x {X:2d} = {(n * X):3d}")
    X = X + 1
