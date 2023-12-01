"""
Listagem 11.20 – Agrupando e contando estados por região
"""
import sqlite3

print("Região Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute(
        """
    select região, count(*)
    from estados
    group by região"""
    ):
        print(f"{regiao[0]:6} {regiao[1]:17d}")
