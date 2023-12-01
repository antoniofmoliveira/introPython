"""
Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
tiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
SOMA = 0
MULT = num2
while MULT > 0:
    SOMA += num1
    MULT -= 1
print(f"{num1} x {num2} = {SOMA}")
