"""
Listagem 9.7 – Controle de uma agenda de telefones

Exercício 9.17 Altere o programa para exibir o tamanho da agenda no menu principal.

Exercício 9.18 O que acontece se nome ou telefone contiverem o caractere usado
como separador em seus conteúdos? Explique o problema e proponha uma solução.

Exercício 9.19 Altere a função lista para que exiba também a posição de cada
elemento.

Exercício 9.20 Adicione a opção de ordenar a lista por nome no menu principal.

Exercício 9.21 Nas funções de altera e apaga, peça que o usuário confirme a alte-
ração e exclusão do nome antes de realizar a operação em si.

Exercício 9.22 Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi
gravada. Você pode usar uma variável para controlar quando a lista foi alterada
(novo, altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.

Exercício 9.23 Altere o programa para ler a última agenda lida ou gravada ao ini-
cializar. Dica: utilize outro arquivo para armazenar o nome.

Exercício 9.24 O que acontece com a agenda se ocorrer um erro de leitura ou
gravação? Explique.

resposta dispara uma exceção

Exercício 9.25 Altere as funções pede_nome e pede_telefone de forma a receberem
um parâmetro opcional. Caso esse parâmetro seja passado, utilize-o como retorno
caso a entrada de dados seja vazia.

Exercício 9.26 Altere o programa de forma a verificar a repetição de nomes. Gere
uma mensagem de erro caso duas entradas na agenda tenham o mesmo nome.

Exercício 9.27 Modifique o programa para também controlar a data de aniversário
e o e-mail de cada pessoa.

Exercício 9.28 Modifique o programa de forma a poder registrar vários telefones
para a mesma pessoa. Permita também cadastrar o tipo de telefone: celular, fixo,
residência, trabalho ou fax.

=== EXERCICIO 9.28 NAO REALIZADO ===

"""
AGENDA = []
ALTERADA = [False]  # 9.22


def pede_nome(nome="default"):  # 9.25
    """_summary_"""
    resposta = input("Nome: ")  # 9.25
    if len(resposta.strip()) == 0:  # 9.25
        return nome  # 9.25
    return resposta  # 9.25


def pede_telefone(telefone="000"):  # 9.25
    """_summary_"""
    resposta = input("Telefone: ")  # 9.25
    if len(resposta.strip()) == 0:  # 9.25
        return telefone  # 9.25
    return resposta  # 9.25


def pede_data_aniversario(data="01/01/1901"):  # 9.27
    """_summary_"""
    resposta = input("Data de aniversário: ")  # 9.27
    if len(resposta.strip()) == 0:  # 9.27
        return data  # 9.27
    return resposta  # 9.27


def pede_email(email="nd"):  # 9.27
    """_summary_"""
    resposta = input("E-mail: ")  # 9.27
    if len(resposta.strip()) == 0:  # 9.27
        return email  # 9.27
    return resposta  # 9.27


def mostra_dados(indice, nome, telefone, aniversario, email):  # 9.19 # 9.27
    """_summary_

    Args:
        nome (_type_): _description_
        telefone (_type_): _description_
    """
    if indice is None:  # 9.19
        print(f"Nome: {nome:20s} Telefone: {telefone:12s}", end="")  # 9.19 # 9.27
        print(f" Aniversário: {aniversario:10s} E-mail: {email:20s}")  # 9.27
    else:  # 9.19
        print(
            f"{indice:d} Nome: {nome:20s} Telefone: {telefone:12s}", end=""
        )  # 9.19 # 9.27
        print(f" Aniversário: {aniversario:10s} E-mail: {email:20s}")  # 9.27


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
    aniversario = pede_data_aniversario()  # 9.27
    email = pede_email()  # 9.27
    jah_existe = False  # 9.26
    for entrada in AGENDA:  # 9.26
        if entrada[0] == nome:  # 9.26
            jah_existe = True  # 9.26
    if jah_existe:  # 9.26
        print("Nome já existe. Escolha a opção alterar")  # 9.26
        return  # 9.26
    AGENDA.append([nome, telefone, aniversario, email])  # 9.27
    ALTERADA[0] = True  # 9.22


def apaga():
    """_summary_"""
    # global AGENDA
    nome = pede_nome()
    pnome = pesquisa(nome)
    if pnome is not None:
        if input("Confirma deleção? (S/N) : ") in ("S", "s"):  # 9.21
            del AGENDA[pnome]  # 9.21
            ALTERADA[0] = True  # 9.22
    else:
        print("Nome não encontrado.")


def altera():
    """_summary_"""
    pnome = pesquisa(pede_nome())
    if pnome is not None:
        nome = AGENDA[pnome][0]
        telefone = AGENDA[pnome][1]
        aniversario = AGENDA[pnome][2]  # 9.27
        email = AGENDA[pnome][3]  # 9.27
        print("Encontrado:")
        mostra_dados(None, nome, telefone, aniversario, email)  # 9.19
        nome = pede_nome()
        telefone = pede_telefone()
        aniversario = pede_data_aniversario()  # 9.27
        email = pede_email()  # 9.27
        if input("Confirma alteração? (S/N) : ") in ("S", "s"):  # 9.21
            AGENDA[pnome] = [nome, telefone, aniversario, email]  # 9.21 # 9.27
            ALTERADA[0] = True  # 9.22
    else:
        print("Nome não encontrado.")


def lista():
    """_summary_"""
    print("\nAgenda\n\n------")
    for indice, entrada in enumerate(AGENDA):  # 9.19
        mostra_dados(indice, entrada[0], entrada[1], entrada[2], entrada[3])  # 9.19
    print("------\n")


def carrega(nome_agenda):  # 9.22
    """_summary_"""
    # global AGENDA
    if ALTERADA[0]:  # 9.22
        print("Agenda alterada. Dados serão perdidos.")  # 9.22
        if input("Confirma? (S/N)") not in ("S", "s"):  # 9.22
            return  # 9.22
    while len(AGENDA) > 0:
        AGENDA.pop()
    if nome_agenda is None:  # 9.23
        nome_arquivo = pede_nome_arquivo()  # 9.23
    else:  # 9.23
        nome_arquivo = nome_agenda  # 9.23
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # AGENDA = []
        for linha in arquivo.readlines():
            # nome, telefone = linha.strip().split("#")
            # nome, telefone = linha.strip().rsplit("#", 1)  # 9.18
            nome, telefone, aniversario, email = linha.strip().rsplit("#", 3)  # 9.27
            AGENDA.append([nome, telefone, aniversario, email])  # 9.27
    # arquivo.close()
    salva_ultima_agenda(nome_arquivo)  # 9.23
    ALTERADA[0] = False  # 9.22


def grava():
    """_summary_"""
    if ALTERADA[0]:  # 9.22
        nome_arquivo = pede_nome_arquivo()
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for entrada in AGENDA:
                arquivo.write(
                    f"{entrada[0]:s}#{entrada[1]:s}#{entrada[2]:s}#{entrada[3]:s}\n"
                )
        salva_ultima_agenda(nome_arquivo)  # 9.23
        ALTERADA[0] = False  # 9.22
    else:  # 9.22
        print("Agenda não foi alterada.")  # 9.22


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


def ordena_nome():  # 9.20
    """_summary_"""
    provisorio = sorted(AGENDA, key=lambda item: item[0])
    while len(AGENDA) > 0:
        AGENDA.pop()
    while len(provisorio) > 0:
        AGENDA.append(provisorio.pop(0))
    ALTERADA[0] = True  # 9.22
    lista()


def salva_ultima_agenda(nome_agenda):  # 9.23
    """_summary_

    Args:
        nome_agenda (_type_): _description_
    """
    with open("agenda.cfg", "w", encoding="utf-8") as config:
        config.write(nome_agenda)


def recupera_ultima_agenda():  # 9.23
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        with open("agenda.cfg", "r", encoding="utf-8") as config:
            return config.readline().strip()
    except FileNotFoundError:
        return None


def menu():
    """
    menu
    """
    print(  # 9.17 # 9.20
        f"""
    Agenda 
    {len(AGENDA)} registro(s) 
        
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê
   7 - Ordenar por nome

   0 - Sai
"""
    )
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)  # 9.20


ultima_agenda = recupera_ultima_agenda()  # 9.23
if ultima_agenda is not None:  # 9.23
    carrega(ultima_agenda)  # 9.23
    print(f"Agenda {ultima_agenda:s} carregada!")  # 9.23
while True:
    opcao = menu()
    if opcao == 0:
        if ALTERADA[0]:  # 9.22
            print("Agenda alterada. Dados serão perdidos.")  # 9.22
            if input("Confirma? (S/N)") in ("s", "s"):  # 9.22
                break  # 9.22

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
        carrega(None)  # 9.23
    elif opcao == 7:  # 9.20
        ordena_nome()  # 9.20
