"""
Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu):
adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da
operação escolhida.
Repita até que a opção saída seja escolhida.
"""
while True:
    print(
        """
    Tabuada
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    S Sair
        """
    )
    opc = input("Selecione a operação: ")
    if opc in ("S", "s"):
        break
    num = float(input("Digite um inteiro maior que 0: "))
    i = 1
    if opc == "+":
        while i <= 10:
            print(f"{num:3.0f} + {i:d} = {(num + i):3.0f}.")
            i += 1
    elif opc == "-":
        while i <= 10:
            print(f"{num:3.0f} - {i:d} = {(num - i):3.0f}.")
            i += 1
    elif opc == "*":
        while i <= 10:
            print(f"{num:3.0f} * {i:d} = {(num * i):3.1f}.")
            i += 1
    elif opc == "/":
        while i <= 10:
            print(f"{num:3.0f} / {i:d} = {(num / i):3.2f}.")
            i += 1
