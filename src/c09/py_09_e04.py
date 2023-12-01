"""
Exercício 9.4 Crie um programa que receba o nome de dois arquivos como pa-
râmetros da linha de comando e que gere um arquivo de saída com as linhas do
primeiro e do segundo arquivo.
"""

import sys

if len(sys.argv) > 3:
    NOME_ARQUIVO1 = sys.argv[1]
    NOME_ARQUIVO2 = sys.argv[2]
    NOME_ARQUIVO3 = sys.argv[3]

    with open(NOME_ARQUIVO1, "r", encoding="utf-8") as arquivo1, open(
        NOME_ARQUIVO2, "r", encoding="utf-8"
    ) as arquivo2, open(NOME_ARQUIVO3, "w", encoding="utf-8") as arquivo3:
        for line in arquivo1.readlines():
            arquivo3.write(line)
        for line in arquivo2.readlines():
            arquivo3.write(line)

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e04",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e04.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["pares.txt", "ímpares.txt", "juntos.txt"]
# }
#     ]
# }
