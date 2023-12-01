"""
Listagem 8.3 – Retornando se valor é par ou não
"""


def ehpar(valor):
    """retorna True se argumento valor é par ou False caso contrário"""
    return valor % 2 == 0


print(ehpar(2))
print(ehpar(3))
print(ehpar(10))
