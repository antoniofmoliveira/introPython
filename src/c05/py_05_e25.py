"""
Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado. Sendo n o nú-
mero a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula
p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e
recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta
entre n e o quadrado de p for menor que 0,0001.
"""
num = float(input("Digite o número para calcular a raiz quadrada: "))
BASE = 2
p = (BASE + (num / BASE)) / 2
while abs(num - p**2) > 0.0001:
    p = (p + (num / p)) / 2
    print(f" {p}")
print(f"informado: {num}, raiz quadrada: {p}, quadrado da raiz: {p**2}")
