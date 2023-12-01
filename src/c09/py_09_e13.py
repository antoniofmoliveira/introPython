"""
Exercício 9.13 Crie um programa que imprima as linhas de um arquivo. Esse pro-
grama deve receber três parâmetros pela linha de comando: o nome do arquivo,
a linha inicial e a última linha a imprimir.
"""

import sys

if len(sys.argv) > 2:
    ARQUIVO = sys.argv[1]
    LINHA_INICIAL = int(sys.argv[2])
    LINHA_FINAL = int(sys.argv[3])
with open(ARQUIVO, "r", encoding="utf-8") as entrada:
    for indice, linha in enumerate(entrada.readlines()):
        if LINHA_INICIAL - 1 <= indice <= LINHA_FINAL - 1:
            print(f"{indice+1:d} - ", end="")
            print(linha.strip())

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e13",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e13.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["entrada2.txt", "10", "20"]
# }
#     ]
# }
