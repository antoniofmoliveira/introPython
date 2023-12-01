"""
Listagem 11.27 – Trabalhando com datas
"""
import sqlite3

with sqlite3.connect("brasil.db", detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    for feriado in conexao.execute("select * from feriados"):
        print(f"{feriado['data'].strftime('%d/%m')} {feriado['descrição']}")
