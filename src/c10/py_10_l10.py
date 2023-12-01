"""
Listagem 10.10 – Criando os objetos
"""
from clientes import Cliente
from bancos import Banco
from contas import Conta

joao = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
jose = Cliente("José Vargas", "9721-3040")
contaJM = Conta([joao, maria], "100")
contaJ = Conta([jose], "10")
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()
