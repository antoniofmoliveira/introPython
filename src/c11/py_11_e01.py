"""
Exercício 11.1 Faça um programa que crie o banco de dados preços.db com a
tabela preços para armazenar uma lista de preços de venda de produtos. A tabela
deve conter o nome do produto e seu respectivo preço. O programa também deve
inserir alguns dados para teste.
"""

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            """
create table lista_precos(
nome_produto text,
preco_produto double)
"""
        )
        artigos = [("merc1", 100.0), ("merc2", 300.5), ("merc3", 55.15)]
        cursor.executemany(
            """
insert into lista_precos (nome_produto, preco_produto)
values(?, ?)
""",
            artigos,
        )
        cursor.execute("select * from lista_precos")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]:s} preço: {resultado[1]:10.2f}")
