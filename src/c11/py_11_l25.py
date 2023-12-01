"""
Listagem 11.25 – Acessando um campo do tipo data
"""
import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    for feriado in conexao.execute("select * from feriados"):
        print(feriado)
