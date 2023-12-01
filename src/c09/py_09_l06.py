"""
Listagem 9.6 – Processamento de um arquivo
"""
LARGURA = 79
# entrada = open("entrada.txt")
with open("entrada.txt", "r", encoding="utf-8") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        if linha[0] == ">":
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == "*":
            print(linha[1:].center(LARGURA))
        else:
            print(linha)
# entrada.close()
