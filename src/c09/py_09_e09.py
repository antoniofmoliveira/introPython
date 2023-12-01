"""
Exercício 9.9 Crie um programa que receba uma lista de nomes de arquivo e os
imprima, um por um.
"""
import sys

if len(sys.argv) > 1:
    NUM_ARQUIVOS = len(sys.argv)
    for indice in range(1, NUM_ARQUIVOS):
        nome_arquivo = sys.argv[indice]
        print(nome_arquivo)
        print(40 * "*")
        with open(nome_arquivo, "r", encoding="utf-8") as entrada:
            # print()
            for linha in entrada.readlines():
                print(linha.strip())
print(40 * "*")

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e09",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e09.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["pares.txt", "paresinv.txt", "ímpares.txt"]
# }
#     ]
# }
