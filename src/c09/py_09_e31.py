"""
Listagem 9.20 – Verificação se um diretório ou arquivo já existe

Exercício 9.31 Crie um programa que corrija o da listagem 9.20 de forma a verificar
se z existe e é um diretório.
"""
import os
import os.path

if os.path.exists("z"):
    print("O diretório z existe.", end="")
    if os.path.isdir("z"):
        print(" E é um diretório.")
    elif os.path.isfile("z"):
        print(" E é um arquivo.")
else:
    print("O diretório z não existe.")
