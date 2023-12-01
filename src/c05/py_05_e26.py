"""
Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira
entre dois números. Utilize apenas as operações de soma e subtração para
calcular o resultado.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

dividendo = num1
divisor = num2

while dividendo >= divisor:
    dividendo = dividendo - divisor
    print(f" {dividendo}")

print(f"{num1} % {num2} = {dividendo}")
