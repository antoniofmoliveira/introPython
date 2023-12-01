"""
Exercício 9.1 Escreva um programa que receba o nome de um arquivo pela linha
de comando e que imprima todas as linhas desse arquivo.
"""
import sys

if len(sys.argv) > 1:
    NOME_ARQUIVO = sys.argv[1]
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            print(linha)

# cd src/c09/
# python py_09_e01.py ../../números.txt

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
        # {
        #     "name": "Python: py_09_e01",
        #     "type": "python",
        #     "request": "launch",
        #     "program": "src/c09/py_09_e01.py",
        #     "console": "integratedTerminal",
        #     "justMyCode": true,
        #     "args": ["números.txt"]
        # },
#     ]
# }
