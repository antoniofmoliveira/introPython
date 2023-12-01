"""
Exercício 3.9 Escreva um programa que leia a quantidade de
dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
"""
dias = int(input("qtde de dias: "))
horas = int(input("qtde de horas: "))
minutos = int(input("qtde de minutos: "))
segundos = int(input("qtde de segundos: "))
total_segundos = segundos
total_segundos += minutos * 60
total_segundos += horas * 60 * 60
total_segundos += dias * 24 * 60 * 60
print(
    f"{dias} dias, {horas} horas, {minutos} minutos e"
    + f" {segundos} segundos são {total_segundos} segundos"
)
