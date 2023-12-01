"""
Listagem 11.26 – Solicitando o tratamento do tipo dos campos
"""
import sqlite3
with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    for feriado in conexao.execute("select * from feriados"):
        print(feriado)
