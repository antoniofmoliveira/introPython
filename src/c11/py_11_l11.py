"""
Listagem 11.11 – Exemplo de update sem where e com rowcount
"""
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            """"update agenda
set telefone = '12345-6789' """
        )
        print("Registros alterados: ", cursor.rowcount)
