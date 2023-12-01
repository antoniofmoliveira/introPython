"""
Exercício 5.19 Modifique o programa para aceitar valores decimais, ou seja,
também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.
"""
valor = float(input("Digite o valor a pagar: "))
CEDULAS = 0
ATUAL = 100
APAGAR = valor
while True:
    if ATUAL <= APAGAR:
        APAGAR -= ATUAL
        CEDULAS += 1
    elif (
        ATUAL == 0.01
        and APAGAR != 0
        and APAGAR < 0.099999999999999999999999999999999999
    ):
        CEDULAS += 1
        APAGAR = 0
    else:
        if ATUAL >= 1:
            print(f"{CEDULAS:d} cédula(s) de R$ {ATUAL:5.2f}.")
        else:
            print(f"{CEDULAS:d} moeda(s) de R$ {ATUAL:5.2f}.")
        if APAGAR == 0:
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
        elif ATUAL == 1:
            ATUAL = 0.5
        elif ATUAL == 0.5:
            ATUAL = 0.1
        elif ATUAL == 0.1:
            ATUAL = 0.05
        elif ATUAL == 0.05:
            ATUAL = 0.02
        elif ATUAL == 0.02:
            ATUAL = 0.01
        CEDULAS = 0
