"""
Exercício 11.6 Escreva um programa que pergunte o nome do produto e um novo
preço. Usando o banco preços.db, atualize o preço deste produto no banco de dados.
"""
import sqlite3
from contextlib import closing

nome = input("Produto a selecionar: ")
no_preco = float(input("Novo preço: "))
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            "update lista_precos set preco_produto = ? where nome_produto = ?",
            (no_preco, nome),
        )
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
