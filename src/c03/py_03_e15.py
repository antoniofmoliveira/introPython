"""
Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
qtde_cigarros = float(input("Informe a quantidade de cigarros por dia: "))
qtde_anos = float(input("Informe a quantidade de anos fumando: "))
total_cigarros = qtde_anos * 365 * qtde_cigarros
total_minutos = total_cigarros * 10
total_dias = total_minutos / (24 * 60)
print(f"Total de dias perdidos: {total_dias:0.1f}")
