"""
Listagem 9.17 – Exclusão de arquivos e diretórios
"""
import os

# Cria um arquivo e o fecha imediatamente
open("morimbundo.txt", "w", encoding="utf-8").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("morimbundo.txt")
