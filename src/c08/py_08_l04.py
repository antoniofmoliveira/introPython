"""
Listagem 8.4 – Reutilização da função épar em outra função
"""


def ehpar(valor):
    """retorna True se argumento valor é par ou False caso contrário"""
    return valor % 2 == 0


def par_ou_impar(valor):
    """
    retorna string 'par' se argumento valor é par
    retorna string 'impar' se argumento valor é impar
    """
    if ehpar(valor):
        return "par"
    # else:
    return "ímpar"


print(par_ou_impar(4))
print(par_ou_impar(5))
