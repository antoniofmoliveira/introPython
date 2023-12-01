"""
Listagem 11.22 – Funções de agregação com order by
"""
import sqlite3

print("Região Estados População  Mínima    Máxima     Média     Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute(
        """
    select região, count(*), min(população), max(população), avg(população),
    sum(população) as tpop
    from estados group by região
    order by tpop desc"""
    ):
        print(
            f"{regiao[0]:6} {regiao[1]:7} {regiao[2]:18,} {regiao[3]:10,} {regiao[4]:10,.0f} {regiao[5]:13,}"
        )
    print(
        "\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
            *conexao.execute(
                """
        select count(*), min(população), max(população),
        avg(população), sum(população) from estados"""
            ).fetchone()
        )
    )
