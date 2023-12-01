"""
Exercício 11.5 Escreva um programa que aumente o preço de todos os produtos
do banco preços.db em 10%.
"""
import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("update lista_precos set preco_produto =  preco_produto * 1.1")
        cursor.execute("select * from lista_precos")
        CONTADOR = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if CONTADOR == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]:s} preço: {resultado[1]:10.2f}")
            CONTADOR += 1
