"""
Listagem 11.15 – Acessando os campos pelo nome
"""
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        for registro in cursor.execute("select * from agenda"):
            print(f"Nome: {registro['nome']:s}\nTelefone: {registro['telefone']:s}")
