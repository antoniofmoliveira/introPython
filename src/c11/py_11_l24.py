"""
Listagem 11.24 – Criando uma tabela de feriados nacionais
"""
import sqlite3

feriados = [
    ["2023-01-01", "Confraternização Universal"],
    ["2023-04-21", "Tiradentes"],
    ["2023-05-01", "Dia do trabalhador"],
    ["2023-09-07", "Independência"],
    ["2023-10-12", "Padroeira do Brasil"],
    ["2023-11-02", "Finados"],
    ["2023-11-15", "Proclamação da República"],
    ["2023-12-25", "Natal"],
]
with sqlite3.connect("brasil.db") as conexao:
    # conexao.execute("delete from feriados")
    conexao.execute(
        "create table feriados(id integer primary key autoincrement, data date, descrição text)"
    )
    conexao.executemany("insert into feriados(data,descrição) values (?,?)", feriados)
