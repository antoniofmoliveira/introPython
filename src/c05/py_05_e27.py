"""
Exercício 5.27 Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501
"""
num = int(input("Digite o número: "))
num2 = num
acc = 0
while num2 > 0:
    r = round(((num2 / 10) - (num2 // 10)) * 10)
    acc = acc * 10 + r
    num2 = num2 // 10
    # print(f" {(num2 / 10)} {r} {acc} {num2}")
# print(f"{int(num)} {int(acc)}")
if round(num) == round(acc):
    print(f"{num} É palíndromo.")
else:
    print(f"{num} NÃO É palíndromo.")
