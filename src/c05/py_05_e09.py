"""
Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
que podemos subtrair 4 cinco vezes de 20.
"""
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
RESTO = num1
QUOC = 0
DIV = num2
while RESTO > 0:
    RESTO -= num2
    QUOC += 1
    DIV -= 1
print(f"{num1} / {num2} = {QUOC}")
