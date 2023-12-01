"""
    Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode
ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor
da casa a comprar dividido pelo número de meses a pagar.
"""
valor_casa = float(input("Digite o valor da casa: "))
valor_salario = float(input("Digite o valor do salario: "))
qtde_anos = float(input("Digite a quantidade de anos: "))
qtde_meses = qtde_anos * 12
valor_parcela = valor_casa / qtde_meses
limite_salario = valor_salario * 30 / 100
if valor_parcela <= limite_salario:
    print(f"Financiamento aprovado. Parcela de R$ {valor_parcela:6.2f}.")
else:
    print("Financiamento NÃO aprovado.")
