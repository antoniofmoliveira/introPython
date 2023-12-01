"""
Listagem 10.8 – Testando Cliente e Contas

Exercício 10.6 Altere o programa de forma que a mensagem saldo insuficiente seja
exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível.

Exercício 10.7 Modifique o método resumo da classe Conta para exibir o nome e
o telefone de cada cliente.

Exercício 10.8 Crie uma nova conta, agora tendo João e José como clientes e saldo
igual a 500.
"""
from clientes import Cliente
from contas import Conta

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
jose = Cliente("jose da Silva", "777-4455")
conta1 = Conta([joao], "1", 1000)
conta2 = Conta([maria, joao], "2", 500)
conta3 = Conta([joao, jose], "3", 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()
conta3.extrato()  # Exercício 10.8
conta2.saque(5000)  # Exercício 10.6
print()
conta1.resumo()  # Exercício 10.7
print()
conta2.resumo()  # Exercício 10.7
print()
conta3.resumo()  # Exercício 10.8
