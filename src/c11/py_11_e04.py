"""
Exercício 11.4
Modifique o programa do exercício 11.3 de forma a perguntar dois
valores e listar todos os produtos com preços entre esses dois valores.
"""
import sqlite3
from contextlib import closing

preco_inicial = float(input("Preço inicial: "))
preco_final = float(input("Preço final: "))
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            "select * from lista_precos where preco_produto between ? and ?",
            (preco_inicial, preco_final),
        )
        CONTADOR = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if CONTADOR == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]:s} preço: {resultado[1]:10.2f}")
            CONTADOR += 1
