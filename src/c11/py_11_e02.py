"""
Exercício 11.2 Faça um programa para listar todos os preços do banco preços.db.
"""

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from lista_precos")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]:s} preço: {resultado[1]:10.2f}")
