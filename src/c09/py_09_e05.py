"""
Exercício 9.5 Crie um programa que inverta a ordem das linhas do arquivo pares.
txt. A primeira linha deve conter o maior número; e a última, o menor.
"""
linhas = []
with open("pares.txt", "r", encoding="utf-8") as pares:
    linhas = pares.readlines()

with open("paresinv.txt", "w", encoding="utf-8") as paresinv:
    for lin in range(len(linhas)-1, -1, -1):
        paresinv.write(linhas[lin])
