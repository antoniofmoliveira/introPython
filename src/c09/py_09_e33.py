"""
Exercício 9.33 Crie um programa que gere uma página html com links para todos
os arquivos jpg e png encontrados a partir de um diretório informado na linha
de comando.
"""
import os
import sys

if len(sys.argv) > 1:
    ALVO = sys.argv[1]
    entradas = os.listdir(ALVO)
    for entrada in entradas:
        if entrada.upper().endswith(
            ("HTML", "TXT")
        ):  # (("PNG", "JPG")):
            print(entrada)


# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e33",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e33.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["src/c09"]
# },
#     ]
# }
