"""
Listagem 10.3 – Verificação da faixa de canais de tv

Exercício 10.3 Modifique a classe Televisão de forma que, se pedirmos para mudar
o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos
para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:

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
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        """_summary_"""
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


tv = Televisao(2, 1, 20)
for x in range(0, 22):
    tv.muda_canal_para_cima()
    print(tv.canal)
for x in range(0, 22):
    tv.muda_canal_para_baixo()
    print(tv.canal)
