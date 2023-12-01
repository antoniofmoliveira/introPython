"""
Exercício 9.2 Modifique o programa do exercício 9.1 para que receba mais dois
parâmetros: a linha de início e a de fim para impressão. O programa deve
imprimir apenas as linhas entre esses dois valores (incluindo as linhas de
início e fim).
"""

import sys

if len(sys.argv) == 4:
    NOME_ARQUIVO = sys.argv[1]
    LINHA_INICIAL = int(sys.argv[2])
    LINHA_FINAL = int(sys.argv[3])
    CONTADOR = 0
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            CONTADOR += 1
            if LINHA_INICIAL <= CONTADOR <= LINHA_FINAL:
                print(linha)

# cd src/c09/
# python py_09_e02.py ../../números.txt 10 20

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
        # {
        #     "name": "Python: py_09_e02",
        #     "type": "python",
        #     "request": "launch",
        #     "program": "src/c09/py_09_e02.py",
        #     "console": "integratedTerminal",
        #     "justMyCode": true,
        #     "args": ["números.txt", "10", "20"]
        # }
#     ]
# }
