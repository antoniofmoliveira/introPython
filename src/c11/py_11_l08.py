"""
Listagem 11.8 – Consulta com filtro de seleção vindo de variável
"""
import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'select * from agenda where nome = "{nome:s}"')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]:s}\nTelefone: {resultado[1]:s}")
