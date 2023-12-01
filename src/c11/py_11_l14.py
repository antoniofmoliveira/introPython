"""
Listagem 11.14 – Consulta vários registros, acesso simplificado
"""
import sqlite3

with sqlite3.connect("agenda.db") as conexao:
    for registro in conexao.execute("select * from agenda"):
        print(f"Nome: {registro[0]:s}\nTelefone: {registro[1]:s}")
