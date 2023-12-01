"""
Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""
valor_inicial = float(input("Valor inicial: "))
taxa_juros = float(input("Taxa de juros mensal: "))
valor_acum = valor_inicial
i = 1
while i <= 24:
    valor_acum += valor_acum * taxa_juros / 100
    print(f"Mês {i:2d} = R$ {valor_acum:6.2f}.")
    i += 1
print(f"Total ganho no período = {(valor_acum - valor_inicial):6.2f}.")
