"""
Exercício 9.3 Crie um programa que leia os arquivos pares.txt e ímpares.txt e
que crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois
arquivos, de forma a preservar a ordem numérica.
"""

with open("ímpares.txt", "r", encoding="utf-8") as impares, open(
    "pares.txt", "r", encoding="utf-8"
) as pares, open("pareseimpares.txt", "w", encoding="utf-8") as pareimpares:
    while True:
        linha = pares.readline()
        if linha.strip() == "":
            break
        pareimpares.write(linha)
        pareimpares.write(impares.readline())
