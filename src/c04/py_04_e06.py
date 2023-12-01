"""
Exercício 4.6
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
"""

distancia = float(input("Digite a distância a percorrer: "))
if distancia <= 200:
    print(f"O valor da passagem será de R$ {distancia*0.5:6.2f}.")
else:
    print(f"O valor da passagem será de R$ {distancia*0.45:6.2f}.")
