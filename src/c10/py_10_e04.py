"""
Listagem 10.3 – Verificação da faixa de canais de tv

Exercício 10.4 Utilizando o que aprendemos com funções, modifique o construtor
da classe Televisão de forma que min e max sejam parâmetros opcionais, onde min
vale 2 e max vale 14, caso outro valor não seja passado.

"""


class Televisao:
    """_summary_"""

    def __init__(self, canal, minimo=2, maximo=14):
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


tv = Televisao(2)
for x in range(0, 22):
    tv.muda_canal_para_cima()
    print(tv.canal)
for x in range(0, 22):
    tv.muda_canal_para_baixo()
    print(tv.canal)
