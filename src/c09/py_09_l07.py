"""
##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem\\capitulo 09\\09.07 - Controle de uma agenda de telefones.py
##############################################################################
"""
AGENDA = []


def pede_nome():
    """_summary_"""
    return input("Nome: ")


def pede_telefone():
    """_summary_"""
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    """_summary_

    Args:
        nome (_type_): _description_
        telefone (_type_): _description_
    """
    print(f"Nome: {nome:s} Telefone: {telefone:s}")


def pede_nome_arquivo():
    """_summary_"""
    return input("Nome do arquivo: ")


def pesquisa(nome):
    """_summary_

    Args:
        nome (_type_): _description_

    Returns:
        _type_: _description_
    """
    mnome = nome.lower()
    for indice, entrada in enumerate(AGENDA):
        if entrada[0].lower() == mnome:
            return indice
    return None


def novo():
    """_summary_"""
    # global AGENDA
    nome = pede_nome()
    telefone = pede_telefone()
    AGENDA.append([nome, telefone])


def apaga():
    """_summary_"""
    # global AGENDA
    nome = pede_nome()
    pnome = pesquisa(nome)
    if pnome is not None:
        del AGENDA[pnome]
    else:
        print("Nome não encontrado.")


def altera():
    """_summary_"""
    pnome = pesquisa(pede_nome())
    if pnome is not None:
        nome = AGENDA[pnome][0]
        telefone = AGENDA[pnome][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        AGENDA[pnome] = [nome, telefone]
    else:
        print("Nome não encontrado.")


def lista():
    """_summary_"""
    print("\nAgenda\n\n------")
    for entrada in AGENDA:
        mostra_dados(entrada[0], entrada[1])
    print("------\n")


def carrega():
    """_summary_"""
    # global AGENDA
    while len(AGENDA) > 0:
        AGENDA.pop()
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # AGENDA = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split("#")
            AGENDA.append([nome, telefone])
    # arquivo.close()


def grava():
    """_summary_"""
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for entrada in AGENDA:
            arquivo.write(f"{entrada[0]:s}#{entrada[1]:s}\n")


def valida_faixa_inteiro(pergunta, inicio, fim):
    """_summary_

    Args:
        pergunta (_type_): _description_
        inicio (_type_): _description_
        fim (_type_): _description_
    """
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio:d} e {fim:d}")


def menu():
    """
    menu
    """
    print(
        """
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê

   0 - Sai
"""
    )
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        carrega()
