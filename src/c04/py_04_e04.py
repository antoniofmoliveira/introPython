"""
Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e
calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule
um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""
salario = float(input("Digite o valor do salário: "))
AUMENTO = 15.0
if salario > 1250.0:
    AUMENTO -= 5.0
print(f"O aumento será de R$ {salario * AUMENTO /100:6.2f}.")
