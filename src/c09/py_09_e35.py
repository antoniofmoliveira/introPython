"""
Exercício 9.35 Utilizando a função os.walk, crie uma página HTML com o nome
e tamanho de cada arquivo de um diretório passado e de seus subdiretórios.
"""

import os
import sys

for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(f" {d:s}/")
    for f in arquivos:
        print(f" {f:s} ({os.path.getsize(os.path.join(raiz, f)):,d} bytes)")
    print(f"{len(diretorios):d} diretório(s), {len(arquivos):d} arquivo(s)")

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_e35",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_e35.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["./src"]
# },
#     ]
# }
