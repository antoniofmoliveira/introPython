"""
Listagem 9.21 – Obtenção de mais informações sobre o arquivo
"""
import os
import os.path
import time
import sys

NOME = sys.argv[1]
print(f"Nome: {NOME:s}")
print(f"Tamanho: {os.path.getsize(NOME):d}")
print(f"Criado: {time.ctime(os.path.getctime(NOME)):s}")
print(f"Modificado: {time.ctime(os.path.getmtime(NOME)):s}")
print(f"Acessado: {time.ctime(os.path.getatime(NOME)):s}")

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
#     "args": ["AGENDA.TXT"]
# },
#     ]
# }
