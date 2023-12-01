"""
Exercício 3.10 Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""
salario = float(input("Valor do salário: "))
percentual = float(input("percentual de aumento: "))
valor_aumento = salario * percentual / 100
valor_salario = salario + valor_aumento
print(
    f"O salario terá uma aumento de {valor_aumento:0.2f} "
    + f"ficando em {valor_salario:0.2f}"
)
