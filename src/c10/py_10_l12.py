"""
Listagem 10.12 – Criação e uso de uma ContaEspecial
"""
from clientes import Cliente
from contas import Conta, ContaEspecial

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
conta1 = Conta([joao], "1", 1000)
conta2 = ContaEspecial([maria, joao], "2", 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
