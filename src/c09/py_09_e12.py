"""
Exercício 9.12 Modifique o programa anterior para também registrar a linha e a
coluna de cada ocorrência da palavra no arquivo. Para isso, utilize listas nos valores
de cada palavra, guardando a linha e a coluna de cada ocorrência.


Exercício 9.11 Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.
"""
dicionario = {}
NUM_LINHA = 0
with open("entrada2.txt", "r", encoding="utf-8") as entrada:
    for linha in entrada.readlines():
        palavras = []
        TMP = ""
        for col, e in enumerate(linha):
            if e.isalnum():
                TMP += e
            else:
                palavras.append([TMP, col - len(TMP)])
                TMP = ""
        NUM_LINHA += 1
        for palavra in palavras:
            if dicionario.get(palavra[0]) is None:
                dicionario[palavra[0]] = [0, []]
            dicionario[palavra[0]][0] += 1
            dicionario[palavra[0]][1].append([NUM_LINHA, palavra[1]])

print(dicionario)
