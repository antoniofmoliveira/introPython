"""
Listagem 10.7 – Conta com registro de operações e extrato (contas.py)

Exercício 10.6 Altere o programa de forma que a mensagem saldo insuficiente seja
exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível.

Exercício 10.7 Modifique o método resumo da classe Conta para exibir o nome e
o telefone de cada cliente.

# Listagem 10.11 – Uso de herança para definir ContaEspecial

Exercício 10.10 Modifique as classes Conta e ContaEspecial para que a operação de
saque retorne verdadeiro se o saque foi efetuado e falso em caso contrário.

Exercício 10.11 Altere a classe ContaEspecial de forma que seu extrato exiba o limite
e o total disponível para saque.

Exercício 10.12 Observe o método saque das classes Conta e ContaEspecial. Modi-
fique o método saque da classe Conta de forma que a verificação da possibilidade
de saque seja feita por um novo método, substituindo a condição atual. Esse
novo método retornará verdadeiro se o saque puder ser efetuado, e falso em caso
contrário. Modifique a classe ContaEspecial de forma a trabalhar com esse novo
método. Verifique se você ainda precisa trocar o método saque de ContaEspecial
ou apenas o novo método criado para verificar a possibilidade de saque.

"""


class Conta:
    """_summary_"""

    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        """_summary_"""
        for cliente in self.clientes:  # Exercício 10.7
            print(f"{cliente.nome:s} - {cliente.telefone:s}")  # Exercício 10.7
        print(f"CC Número: {self.numero:s} Saldo: {self.saldo:10.2f}")

    def pode_sacar(self, valor):  # Exercício 10.12
        """_summary_

        Args:
            valor (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.saldo >= valor

    def saque(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_
        """
        if self.pode_sacar(valor):  # Exercício 10.12
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True  # Exercício 10.10
        else:  # Exercício 10.6
            print("Saldo insuficiente!")  # Exercício 10.6
            return False  # Exercício 10.10

    def deposito(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_
        """
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        """_summary_"""
        print(f"Extrato CC N° {self.numero:s}\n")
        for operacao in self.operacoes:
            print(f"{operacao[0]:10s} {operacao[1]:10.2f}")
        print(f"\nSaldo: {self.saldo:10.2f}\n")


# Listagem 10.11 – Uso de herança para definir ContaEspecial


class ContaEspecial(Conta):
    """_summary_

    Args:
        Conta (_type_): _description_
    """

    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def pode_sacar(self, valor):  # # Exercício 10.12
        return self.saldo + self.limite >= valor

    #  # Exercício 10.12 torna o metodo desnecessário
    # def saque(self, valor):
    #     if self.saldo + self.limite >= valor:
    #         self.saldo -= valor
    #         self.operacoes.append(["SAQUE", valor])
    #         return True  # Exercício 10.10
    #     return False  # Exercício 10.10

    def extrato(self):  # Exercício 10.11
        """_summary_"""
        super().extrato()
        print(f"Limite da conta especial: {self.limite:10.2f}")
        print(f"Disponível para saque:    {self.limite+self.saldo:10.2f}")
