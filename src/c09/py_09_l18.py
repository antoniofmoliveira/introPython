"""
Listagem 9.18 – Listagem do nome de arquivos e diretórios
"""
import os

print(os.listdir("."))
print(os.listdir("avô"))
print(os.listdir("avô/pai"))
print(os.listdir("avô/mãe"))
