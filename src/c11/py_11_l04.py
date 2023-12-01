"""
Listagem 11.4 – Consulta com múltiplos resultados
"""
import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()
for registro in resultado:
    print(f"Nome: {registro[0]:s}\nTelefone: {registro[1]:s}")
cursor.close()
conexao.close()
