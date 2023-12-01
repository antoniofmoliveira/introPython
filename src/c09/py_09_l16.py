"""
Listagem 9.16 – Alteração do nome de arquivos e diretórios
"""
import os

os.makedirs("avô/pai/filho")
os.makedirs("avô/mãe/filha")
os.rename("avô/pai/filho", "avô/mãe/filho")
