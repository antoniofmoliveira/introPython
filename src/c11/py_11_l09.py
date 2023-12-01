"""
Listagem 11.9 – Consulta utilizando parâmetros
"""
import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = ?", (nome,))
        CONTADOR = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if CONTADOR == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]:s}\nTelefone: {resultado[1]:s}")
            CONTADOR += 1
