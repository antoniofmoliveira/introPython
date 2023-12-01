"""
Exercício 9.10 Crie um programa que receba uma lista de nomes de arquivo e que
gere apenas um grande arquivo de saída.
"""
import sys

if len(sys.argv) > 2:
    ARQUIVO_SAIDA = sys.argv[1]
    NUM_ARQUIVOS = len(sys.argv)
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
        for indice in range(2, NUM_ARQUIVOS):
            nome_arquivo = sys.argv[indice]
            saida.write(nome_arquivo + "\n")
            saida.write(40 * "*" + "\n")
            with open(nome_arquivo, "r", encoding="utf-8") as entrada:
                # print()
                for linha in entrada.readlines():
                    saida.write(linha)
        saida.write(40 * "*" + "\n")

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e10",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e10.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["SAIDA.TXT", "pares.txt", "paresinv.txt", "ímpares.txt"]
# }
#     ]
# }
