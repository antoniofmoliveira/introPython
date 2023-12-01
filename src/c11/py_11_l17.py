"""
Listagem 11.17 – Consulta dos estados brasileiros, ordenados por nome
"""
import sqlite3
from contextlib import closing

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        for estado in conexao.execute(
            "select * from estados order by população desc"
        ):  # by nome, by população, by população desc
            print(f"{estado['id']:3d} {estado['nome']:20s} {estado['população']:12d}")
