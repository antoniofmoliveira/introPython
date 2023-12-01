"""
Listagem 11.5 – Consulta, registro por registro
"""
import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f"Nome: {resultado[0]:s}\nTelefone: {resultado[1]:s}")
cursor.close()
conexao.close()
