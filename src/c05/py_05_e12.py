"""
Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e
você deve considerá-lo para o cálculo de juros do mês seguinte.
"""
valor_inicial = float(input("Valor inicial: "))
valor_mensal = float(input("Valor depósito mensal: "))
taxa_juros = float(input("Taxa de juros mensal: "))
valor_acum = valor_inicial
i = 1
while i <= 24:
    valor_acum += valor_acum * taxa_juros / 100
    print(f"Mês {i:2d} = R$ {valor_acum:6.2f}.")
    if i < 24:
        valor_acum += valor_mensal
    i += 1
print(f"Total ganho no período = {(valor_acum - valor_inicial):6,.2f}.")
