"""
Listagem 9.3 – Impressão dos parâmetros passados na linha de comando
"""
import sys

print(f"Número de parâmetros: {len(sys.argv):d}")
for indice, parametro in enumerate(sys.argv):
    print(f"Parâmetro {indice:d} = {parametro:s}")
