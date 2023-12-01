"""
Listagem 10.5 – Programa teste.py que importa a classe Cliente (clientes.py)
"""
from clientes import Cliente
from contas import Conta

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

print(joao.nome)
print(joao.telefone)

print(maria.nome)
print(maria.telefone)

conta = Conta(joao, numero="1", saldo=5000)
conta.resumo()
conta.saque(1000)
conta.resumo()
conta.saque(50)
conta.resumo()
conta.deposito(200)
conta.resumo()
