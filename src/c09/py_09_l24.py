"""
Listagem 9.24 – Uso de caminhos
"""
import os.path

CAMINHO = "i/j/k"
print(os.path.abspath(CAMINHO))

print(os.path.basename(CAMINHO))
print(os.path.dirname(CAMINHO))
print(os.path.split(CAMINHO))
print(os.path.splitext("arquivo.txt"))
print(os.path.splitdrive("c:/Windows"))
