"""
Exercício 9.11 Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.
"""
dicionario = {}
with open("entrada2.txt", "r", encoding="utf-8") as entrada:
    for linha in entrada.readlines():
        palavras = linha.split()
        for palavra in palavras:
            dicionario[palavra] = dicionario.get(palavra, 0) + 1
print(dicionario)
