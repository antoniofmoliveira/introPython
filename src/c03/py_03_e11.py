"""
Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria
e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
"""
valor_mercadoria = float(input("Valor da mercadoria: "))
percentual = float(input("percentual de desconto: "))
valor_desconto = valor_mercadoria * percentual / 100
novo_valor_mercadoria = valor_mercadoria - valor_desconto
print(
    f"A mercadoria terá um desconto de {valor_desconto:0.2f} "
    + f"ficando em {novo_valor_mercadoria:0.2f}"
)
