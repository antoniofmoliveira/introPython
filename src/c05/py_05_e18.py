"""
Exercício 5.18 Modifique o programa para também trabalhar com notas de R$ 100.
"""
valor = int(input("Digite o valor a pagar: "))
CEDULAS = 0
ATUAL = 100
apagar = valor
while True:
    if ATUAL <= apagar:
        apagar -= ATUAL
        CEDULAS += 1
    else:
        print(f"{CEDULAS:d} cédula(s) de R$ {ATUAL:d}.")
        if apagar == 0:
            break
        if ATUAL == 100:
            ATUAL = 50
        elif ATUAL == 50:
            ATUAL = 20
        elif ATUAL == 20:
            ATUAL = 10
        elif ATUAL == 10:
            ATUAL = 5
        elif ATUAL == 5:
            ATUAL = 1
        CEDULAS = 0
