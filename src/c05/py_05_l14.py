"""
Listagem 5.14 - Contagem de cédulas
"""
valor = int(input("Digite o valor a pagar: "))
CEDULAS = 0
ATUAL = 50
apagar = valor
while True:
    if ATUAL <= apagar:
        apagar -= ATUAL
        CEDULAS += 1
    else:
        print(f"{CEDULAS:d} cédula(s) de R$ {ATUAL:d}.")
        if apagar == 0:
            break
        if ATUAL == 50:
            ATUAL = 20
        elif ATUAL == 20:
            ATUAL = 10
        elif ATUAL == 10:
            ATUAL = 5
        elif ATUAL == 5:
            ATUAL = 1
        CEDULAS = 0
