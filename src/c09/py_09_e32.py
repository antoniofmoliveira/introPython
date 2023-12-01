"""
Listagem 9.20 – Verificação se um diretório ou arquivo já existe

Exercício 9.32 Modifique o programa da listagem 9.20 de forma a receber o nome
do arquivo ou diretório a verificar pela linha de comando. Imprima se existir e se
for um arquivo ou um diretório.
"""
import os
import os.path
import sys

if len(sys.argv) > 1:
    ALVO = sys.argv[1]
    if os.path.exists(ALVO):
        print("O diretório z existe.", end="")
        if os.path.isdir(ALVO):
            print(" E é um diretório.")
        elif os.path.isfile(ALVO):
            print(" E é um arquivo.")
    else:
        print("O diretório z não existe.")


# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e32",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e32.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["números.txt"]
# },
#     ]
# }
