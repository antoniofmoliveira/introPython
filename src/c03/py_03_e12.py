"""
Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""
distancia = float(input("Distancia a ser percorrida: "))
vel_media = float(input("Velocidade média esperada: "))
tempo_horas = distancia // vel_media
resto_minutos = (distancia / vel_media - tempo_horas) * 60
print(
    f"Essa viagem deve demorar {tempo_horas:0.0f} horas "
    + f"e {resto_minutos:0.0f} minutos."
)
