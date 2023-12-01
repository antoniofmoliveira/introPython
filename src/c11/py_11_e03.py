"""
Exercício 11.3
Escreva um programa que realize consultas do banco de dados
preços.db, criado no exercício 11.1. O programa deve perguntar o nome do produto
e listar seu preço.
"""
import sqlite3
from contextlib import closing

nome = input("Produto a selecionar: ")
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from lista_precos where nome_produto = ?", (nome,))
        CONTADOR = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if CONTADOR == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]:s} preço: {resultado[1]:10.2f}")
            CONTADOR += 1
