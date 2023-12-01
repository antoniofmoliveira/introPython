"""
Listagem 9.19 – Verificação se é diretório ou arquivo
"""
import os
import os.path

for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a:s}/")
    elif os.path.isfile(a):
        print(f"{a:s}")
