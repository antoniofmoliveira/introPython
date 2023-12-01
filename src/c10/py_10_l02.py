"""
Listagem 10.2 – Adição de métodos para mudar o canal
"""


class Televisao:
    """_summary_"""

    def __init__(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        """_summary_"""
        self.canal -= 1

    def muda_canal_para_cima(self):
        """_summary_"""
        self.canal += 1


tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
