"""
Listagem 11.13 – Apagando registros
"""
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            """delete from agenda
where nome = 'Maria' """
        )
        print("Registros apagados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
            print("Alterações gravadas")
        else:
            conexao.rollback()
        print("Alterações abortadas")
