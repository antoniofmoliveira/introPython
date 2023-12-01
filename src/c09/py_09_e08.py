"""
Exercício 9.8 Modifique o programa anterior para também receber o número de
caracteres por linha e o número de páginas por folha pela linha de comando.


Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
terá no máximo 60 linhas. Adicione na última linha de cada página o número da
página atual e o nome do arquivo original.
"""

import sys

NUM_PAG = 1
NUM_LINHA = 0
NOME_ARQUIVO_ENTRADA = "entrada2.txt"
NOME_ARQUIVO_SAIDA = "saida.txt"
NUM_LIN_PAGE = 60
NUM_CARAC_LIN = 76
if len(sys.argv) == 5:
    NOME_ARQUIVO_ENTRADA = sys.argv[1]
    NOME_ARQUIVO_SAIDA = sys.argv[2]
    NUM_LIN_PAGE = int(sys.argv[3])
    NUM_CARAC_LIN = int(sys.argv[4])
with open(NOME_ARQUIVO_ENTRADA, "r", encoding="utf-8") as entrada, open(
    NOME_ARQUIVO_SAIDA, "w", encoding="utf-8"
) as saida:
    for linha in entrada.readlines():
        temp_linha = linha
        while len(temp_linha) > 0:
            parte_linha = temp_linha[0 : (NUM_CARAC_LIN - 1)]
            parte_linha = parte_linha.strip() + "\n"
            saida.write(parte_linha)
            temp_linha = temp_linha[NUM_CARAC_LIN:]
            NUM_LINHA += 1
            if NUM_LINHA > NUM_LIN_PAGE:
                saida.write(f"\npágina: {NUM_PAG:d} - {NOME_ARQUIVO_SAIDA:s}\n\n")
                NUM_PAG += 1
                NUM_LINHA = 0
    if NUM_LINHA != NUM_LIN_PAGE:
        saida.write(f"\npágina: {NUM_PAG:d} - {NOME_ARQUIVO_SAIDA:s}\n")
        NUM_PAG += 1
        NUM_LINHA = 0

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e08",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e08.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["entrada2.txt", "saida2.txt", "50", "70"]
# }
#     ]
# }
