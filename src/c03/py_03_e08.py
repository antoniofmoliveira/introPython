"""
Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba
convertido em milímetros.
"""
qtde_metros = float(input("Quantidade de metros: "))
qtde_milimetros = qtde_metros * 1000.0
print(f"{qtde_metros:0.0f} metros igual a {qtde_milimetros:0.0f} milímetros.")
