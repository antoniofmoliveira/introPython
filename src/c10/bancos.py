"""
Listagem 10.9 – Classe Banco (bancos.py)
"""


class Banco:
    """_summary_
    """
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        """_summary_

        Args:
            conta (_type_): _description_
        """
        self.contas.append(conta)

    def lista_contas(self):
        """_summary_
        """
        for conta in self.contas:
            conta.resumo()
