"""
Exercício 9.36 Utilizando a função os.walk, crie um programa que calcule o es-
paço ocupado por cada diretório e subdiretório, gerando uma página html com
os resultados.
"""

import os
import sys

for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print(f"Caminho: {raiz:s}", end="")
    ACC = 0
    for f in arquivos:
        ACC += os.path.getsize(os.path.join(raiz, f))
    print(f" ({ACC:,d} bytes)")

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e36",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e36.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["./src"]
# },
#     ]
# }
