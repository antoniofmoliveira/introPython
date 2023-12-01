"""Exercício 5.15 Escreva um programa para controlar uma pequena máquina
registradora. Você deve solicitar ao usuário que digite o código do produto e
a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço
de cada produto:
    Código  Preço
    1       0,50
    2       1,00
    3       4,00
    5       7,00
    9       8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
"""

S = 0
while True:
    v = float(input("Digite o código da mercadoria ou 0 para sair: "))
    if v == 0:
        break
    elif v == 1:
        S += 0.5
    elif v == 2:
        S += 1.0
    elif v == 3:
        S += 4.0
    elif v == 5:
        S += 7.0
    elif v == 9:
        S += 8.0
    else:
        print("Código inválido!")
    print(f"subtotal da compra é R$ {S:6,.2f}.")
print(f"Total da compra é R$ {S:6,.2f}.")
