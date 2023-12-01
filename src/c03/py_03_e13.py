"""Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:
F = (9 * C) / 5 + 32
"""
temp_c = float(input("Informe a temperatura em °C: "))
temp_f = (9.0 * temp_c) / 5.0 + 32.0
print(f"{temp_c:0.2F}°C equivale a {temp_f:0.2f}°F.")
