"""
Exercício 5.24 Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
"""
qtde_desejada = int(input("Digite quantidade de primos desejada: "))
CONTADOR = 0
LACO = 2
while CONTADOR < qtde_desejada:
    NUM = LACO
    if NUM == 0:
        break
    if NUM == 2:
        print("2 ", end="")
        CONTADOR += 1
    else:
        i = 3
        EH_PRIMO = False
        while i <= NUM:
            if NUM % i == 0 and i == NUM:
                EH_PRIMO = True
                break
            if NUM % i == 0 and i != NUM:
                break
            i += 2
        if EH_PRIMO:
            print(f"{NUM:d} ", end="")
            CONTADOR += 1
    LACO += 1
print("")
