"""
Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não
um número primo. Para fazer essa verificação, calcule o resto da divisão do
número por 2 e depois por todos os números ímpares até o número lido. Se o
resto de uma dessas divisões for igual a zero, o número não é primo. Observe
que 0 e 1 não são primos e que 2 é o único número primo que é par.
"""
while True:
    num = int(input("Digite número > 1 a ser checado ou 0 para sair: "))
    if num == 0:
        break
    if num == 2:
        print(" 2 é primo")
    elif num % 2 == 0:
        print(f"{num:d} NÃO é primo.")
    else:
        i = 3
        EH_PRIMO = False
        while i <= num:
            if num % i == 0 and i == num:
                EH_PRIMO = True
                break
            if num % i == 0 and i != num:
                break
            i += 2
        if EH_PRIMO:
            print(f"{num:d} É primo.")
        else:
            print(f"{num:d} NÃO é primo.")
