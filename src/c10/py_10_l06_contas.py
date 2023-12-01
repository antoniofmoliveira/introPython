"""
Listagem 10.6 – Classe Conta (contas.py)
"""


class Conta:
    """_summary_"""

    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero

    def resumo(self):
        """_summary_"""
        print(f"CC Número: {self.numero:s} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_
        """
        if self.saldo >= valor:
            self.saldo -= valor

    def deposito(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_
        """
        self.saldo += valor
