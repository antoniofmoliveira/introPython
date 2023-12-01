"""
Listagem 8.35 – Módulo soma (soma.py) que importa entrada
"""
import entrada

LISTA = []
for x in range(10):
    LISTA.append(entrada.valida_inteiro("Digite um número:", 0, 20))
print(f"Soma: {(sum(LISTA)):d}")
