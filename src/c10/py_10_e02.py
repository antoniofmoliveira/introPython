"""
Listagem 10.3 – Verificação da faixa de canais de tv

Exercício 10.2 Atualmente, a classe Televisão inicializa o canal com 2. Modifique
a classe Televisão de forma a receber o canal inicial em seu construtor.

"""


class Televisao:
    """_summary_"""

    def __init__(self, canal, minimo, maximo):
        self.ligada = False
        self.canal = canal
        self.cmin = minimo
        self.cmax = maximo

    def muda_canal_para_baixo(self):
        """_summary_"""
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        """_summary_"""
        if self.canal + 1 <= self.cmax:
            self.canal += 1


tv = Televisao(2, 1, 20)
for x in range(0, 22):
    tv.muda_canal_para_cima()
    print(tv.canal)
for x in range(0, 22):
    tv.muda_canal_para_baixo()
    print(tv.canal)
