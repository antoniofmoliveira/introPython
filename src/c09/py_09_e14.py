"""
Exercício 9.14 Crie um programa que leia um arquivo-texto e elimine os espaços
repetidos entre as palavras e no fim das linhas. O arquivo de saída também não
deve ter mais de uma linha em branco repetida.
"""

with open("entrada2.txt", "r", encoding="utf-8") as entrada, open(
    "saida3.txt", "w", encoding="utf-8"
) as saida:
    LINHA_ANT = False
    for linha in entrada.readlines():
        TMP = ""
        ANT = ""
        for e in linha.strip():
            if ANT != " " or (ANT == " " and e != " "):
                TMP += e
                ANT = e
        TMP += "\n"
        if LINHA_ANT and TMP == "\n":
            continue
        LINHA_ANT = TMP == "\n"
        saida.write(TMP)
