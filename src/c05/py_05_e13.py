"""
Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago.
"""
valor_inicial = float(input("Valor inicial da dívida: "))
valor_mensal = float(input("Valor pagamento mensal: "))
taxa_juros = float(input("Taxa de juros mensal: "))
VALOR_RESIDUAL = valor_inicial
TOTAL_PAGO = 0
QTDE_MESES = 0
while VALOR_RESIDUAL > 0:
    VALOR_RESIDUAL += VALOR_RESIDUAL * taxa_juros / 100
    if VALOR_RESIDUAL > valor_mensal:
        TOTAL_PAGO += valor_mensal
        VALOR_RESIDUAL -= valor_mensal
    else:
        TOTAL_PAGO += VALOR_RESIDUAL
        VALOR_RESIDUAL = 0
    QTDE_MESES += 1
print(f"Quantidade de meses: {QTDE_MESES}.")
print(f"Valor total pago: R$ {TOTAL_PAGO:6,.2f}.")
print(f"Total juros pago: R$ {(TOTAL_PAGO - valor_inicial):6,.2f}.")
