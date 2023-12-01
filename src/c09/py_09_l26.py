"""
Listagem 9.26 – Árvore de diretórios sendo percorrida
"""
import os
import sys

for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(f" {d:s}/")
    for f in arquivos:
        print(f" {f:s}")
    print(f"{len(diretorios):d} diretório(s), {len(arquivos):d} arquivo(s)")

# launch.json
# {
#     "version": "0.2.0",
#     "configurations": [
# {
#     "name": "Python: py_09_l26",
#     "type": "python",
#     "request": "launch",
#     "program": "src/c09/py_09_l26.py",
#     "console": "integratedTerminal",
#     "justMyCode": true,
#     "args": ["./src"]
# },
#     ]
# }
