"""
Listagem 10.1 – Modelagem de uma televisão

Exercício 10.1 Adicione os atributos tamanho e marca à classe Televisão. Crie
dois objetos Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o
valor desses atributos de forma a confirmar a independência dos valores de cada
instância (objeto).
"""


class Televisao:
    """_summary_"""

    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 30
        self.marca = ""


tv = Televisao()
tv.marca = "Sony"
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.tamanho = 50
tv_sala.marca = "Samsung"
print(tv.ligada)
print(tv.canal)
print(tv.tamanho)
print(tv.marca)
print(tv_sala.ligada)
print(tv_sala.canal)
print(tv_sala.tamanho)
print(tv_sala.marca)
