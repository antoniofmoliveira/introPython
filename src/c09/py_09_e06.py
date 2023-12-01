"""
Exercício 9.6 Modifique o programa da listagem 9.6 para imprimir 40 vezes o
símbolo de = se este for o primeiro caractere da linha. Adicione também a opção
para parar de imprimir até que se pressione a tecla Enter cada vez que uma
linha iniciar com . como primeiro caractere.
"""

LARGURA = 79
with open("entrada.txt", "r", encoding="utf-8") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        if linha[0] == ">":
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == "*":
            print(linha[1:].center(LARGURA))
        elif linha[0] == ".":
            input("Tecle ENTER para prosseguir.")
            print(40 * "=")
        else:
            print(linha)
