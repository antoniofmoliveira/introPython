"""
Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60
por dia e R$ 0,15 por km rodado.
"""
qtde_km = float(input("Informe a quantidade de km rodados: "))
qtde_dias = float(input("Informe a quantidade de dias de aluguel: "))
valor_km = qtde_km * 0.15
valor_aluguel = qtde_dias * 60.0
preco_a_pagar = valor_aluguel + valor_km
print(f"O valor a pagar é de R$ {preco_a_pagar:0.2f}")
