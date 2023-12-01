"""
Exercício 10.9 Crie classes para representar estados e cidades. Cada estado tem um
nome, sigla e cidades. Cada cidade tem nome e população. Escreva um programa de
testes que crie três estados com algumas cidades em cada um. Exiba a população
de cada estado como a soma da população de suas cidades.
"""


class Estado:
    """_summary_"""

    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def populacao(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        populacao_estado = 0
        for cidade in self.cidades:
            populacao_estado += cidade.populacao
        return populacao_estado


class Cidade:
    """_summary_"""

    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao


estado1 = Estado(
    "Estado 1",
    "E1",
    [
        Cidade("Cidade1", 100),
        Cidade("Cidade2", 200),
        Cidade("Cidade3", 300),
        Cidade("Cidade4", 400),
    ],
)
estado2 = Estado(
    "Estado 2",
    "E2",
    [
        Cidade("Cidade5", 500),
        Cidade("Cidade6", 600),
        Cidade("Cidade7", 700),
        Cidade("Cidade8", 800),
    ],
)
estado3 = Estado(
    "Estado 3",
    "E3",
    [
        Cidade("Cidade9", 900),
        Cidade("Cidade10", 1000),
        Cidade("Cidade11", 1100),
        Cidade("Cidade12", 1200),
    ],
)

estados = [estado1, estado2, estado3]

for estado in estados:
    print(f"{estado.nome:s} ({estado.sigla:s}) : {estado.populacao():,d} habitantes.")
