"""
Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = num1
menor = num1

if num1 >= num2 and num1 >= num3:
    maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior = num3
if num1 <= num2 and num1 <= num3:
    menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor = num3

print(f"Maior: {maior} e Menor: {menor}.")
