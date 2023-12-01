"""
Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+),
subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da
operação solicitada.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
oper = input("Digite a operação ( + - * / ): ")
if oper == "+":
    print(f"{num1} {oper} {num2} = {num1 + num2}")
elif oper == "-":
    print(f"{num1} {oper} {num2} = {num1 - num2}")
elif oper == "*":
    print(f"{num1} {oper} {num2} = {num1 * num2}")
elif oper == "/":
    if num2 == 0:
        print("Não pode dividir por 0.")
    else:
        print(f"{num1} {oper} {num2} = {num1 / num2}")
else:
    print("Operação não reconhecida.")
