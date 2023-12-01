"""
Listagem 11.31 – Agenda com banco de dados completo
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
# Arquivo: listagem\capitulo 11\11.31 - Agenda com banco de dados completo.py
##############################################################################

import sys
import sqlite3
import os.path
from functools import total_ordering

BANCO = """
create table tipos(id integer primary key autoincrement,
                   descrição text);
create table nomes(id integer primary key autoincrement,
                   nome text);
create table telefones(id integer primary key autoincrement,
                   id_nome integer,
                   número text,
                   id_tipo integer);
insert into tipos(descrição) values ("Celular");
insert into tipos(descrição) values ("Fixo");
insert into tipos(descrição) values ("Fax");
insert into tipos(descrição) values ("Casa");
insert into tipos(descrição) values ("Trabalho");
"""


def nulo_ou_vazio(texto):
    """_summary_

    Args:
        texto (_type_): _description_

    Returns:
        _type_: _description_
    """
    return texto is None or not texto.strip()


def valida_faixa_inteiro(pergunta, inicio, fim, padrao=None):
    """_summary_

    Args:
        pergunta (_type_): _description_
        inicio (_type_): _description_
        fim (_type_): _description_
    """
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao is not None:
                entrada = padrao
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio:d} e {fim:d}")


def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    """_summary_

    Args:
        pergunta (_type_): _description_
        inicio (_type_): _description_
        fim (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio:d} e {fim:d}")


class ListaUnica:
    """_summary_"""

    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def __getitem__(self, indice):
        return self.lista[indice]

    def indice_valido(self, indice):
        """_summary_

        Args:
            indice (_type_): _description_

        Returns:
            _type_: _description_
        """
        return indice >= 0 and indice < len(self.lista)

    def adiciona(self, elem):
        """_summary_

        Args:
            elem (_type_): _description_
        """
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        """_summary_

        Args:
            elem (_type_): _description_
        """
        self.lista.remove(elem)

    def pesquisa(self, elem):
        """_summary_

        Args:
            elem (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        """_summary_

        Args:
            elem (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if isinstance(elem, self.elem_class):  # type(elem) != self.elem_class:
            raise TypeError("Tipo inválido")

    def ordena(self, chave=None):
        """_summary_

        Args:
            chave (_type_, optional): _description_. Defaults to None.
        """
        self.lista.sort(key=chave)


class DBListaUnica(ListaUnica):
    """_summary_"""

    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.apagados = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        """_summary_"""
        self.apagados = []


@total_ordering
class Nome:
    """_summary_"""

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.__nome} Chave: {self.__chave}>"

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.cria_chave(valor)

    @property
    def chave(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__chave

    @staticmethod
    def cria_chave(nome):
        """_summary_

        Args:
            nome (_type_): _description_

        Returns:
            _type_: _description_
        """
        return nome.strip().lower()


class DBNome(Nome):
    """_summary_

    Args:
        Nome (_type_): _description_
    """

    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_


@total_ordering
class TipoTelefone:
    """_summary_"""

    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "f({self.tipo})"

    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo

    def __lt__(self, outro):
        return self.tipo < outro.tipo


class DBTipoTelefone(TipoTelefone):
    """_summary_

    Args:
        TipoTelefone (_type_): _description_
    """

    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_


class Telefone:
    """_summary_"""

    def __init__(self, numero, tipo=None):
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        if self.tipo is not None:
            tipo = self.tipo
        else:
            tipo = ""
        return f"{self.numero} {tipo}"

    def __eq__(self, outro):
        return self.numero == outro.número and (
            (self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None)
        )

    @property
    def numero(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Número não pode ser None ou em branco")
        self.__numero = valor


class DBTelefone(Telefone):
    """_summary_

    Args:
        Telefone (_type_): _description_
    """

    def __init__(self, numero, tipo=None, id_=None, id_nome=None):
        super().__init__(numero, tipo)
        self.id = id_
        self.id_nome = id_nome


class DBTelefones(DBListaUnica):
    """_summary_

    Args:
        DBListaUnica (_type_): _description_
    """

    def __init__(self):
        super().__init__(DBTelefone)


class DBTiposTelefone(ListaUnica):
    """_summary_

    Args:
        ListaUnica (_type_): _description_
    """

    def __init__(self):
        super().__init__(DBTipoTelefone)


class DBDadoAgenda:
    """_summary_"""

    def __init__(self, nome):
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, DBNome):  # type(valor) != DBNome:
            raise TypeError("nome deve ser uma instância da classe DBNome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        """_summary_

        Args:
            telefone (_type_): _description_

        Returns:
            _type_: _description_
        """
        posicao = self.telefones.pesquisa(DBTelefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]


class DBAgenda:
    """_summary_"""

    def __init__(self, banco):
        self.tipos_telefone = DBTiposTelefone()
        self.banco = banco
        novo = not os.path.isfile(banco)
        self.conexao = sqlite3.connect(banco)
        self.conexao.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carrega_tipos()

    def carrega_tipos(self):
        """_summary_"""
        for tipo in self.conexao.execute("select * from tipos"):
            id_ = tipo["id"]
            descrição = tipo["descrição"]
            self.tipos_telefone.adiciona(DBTipoTelefone(id_, descrição))

    def cria_banco(self):
        """_summary_"""
        self.conexao.executescript(BANCO)

    def pesquisa_nome(self, nome):
        """_summary_"""
        if not isinstance(nome, DBNome):
            raise TypeError("nome deve ser do tipo DBNome")
        achado = self.conexao.execute(
            """select count(*) from nomes where nome = ?""",
            (nome.nome,),
        ).fetchone()
        if achado[0] > 0:
            return self.carrega_por_nome(nome)
        # else:
        return None

    def carrega_por_id(self, id):
        """_summary_

        Args:
            id (_type_): _description_

        Returns:
            _type_: _description_
        """
        consulta = self.conexao.execute("select * from nomes where id = ?", (id,))
        return self.carrega(consulta.fetchone())

    def carrega_por_nome(self, nome):
        """_summary_

        Args:
            nome (_type_): _description_

        Returns:
            _type_: _description_
        """
        consulta = self.conexao.execute(
            "select * from nomes where nome = ?", (nome.nome,)
        )
        return self.carrega(consulta.fetchone())

    def carrega(self, consulta):
        """_summary_

        Args:
            consulta (_type_): _description_

        Returns:
            _type_: _description_
        """
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta["nome"], consulta["id"]))
        for telefone in self.conexao.execute(
            "select * from telefones where id_nome = ?", (novo.nome.id,)
        ):
            ntel = DBTelefone(
                telefone["número"], None, telefone["id"], telefone["id_nome"]
            )
            for tipo in self.tipos_telefone:
                if tipo.id == telefone["id_tipo"]:
                    ntel.tipo = tipo
                    break
            novo.telefones.adiciona(ntel)
        return novo

    def lista(self):
        """_summary_

        Yields:
            _type_: _description_
        """
        consulta = self.conexao.execute("select * from nomes order by nome")
        for registro in consulta:
            yield self.carrega(registro)

    def novo(self, registro):
        """_summary_"""
        try:
            cur = self.conexao.cursor()
            cur.execute("insert into nomes(nome) values (?)", (str(registro.nome),))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute(
                    """insert into telefones(número,
                               id_tipo, id_nome) values (?,?,?)""",
                    (telefone.número, telefone.tipo.id, registro.nome.id),
                )
                telefone.id = cur.lastrowid
            self.conexao.commit()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()

    def atualiza(self, registro):
        """_summary_"""
        try:
            cur = self.conexao.cursor()
            cur.execute(
                "update nomes set nome=? where id = ?",
                (str(registro.nome), registro.nome.id),
            )
            for telefone in registro.telefones:
                if telefone.id is None:
                    cur.execute(
                        """insert into telefones(número,
                                   id_tipo, id_nome)
                                   values (?,?,?)""",
                        (telefone.número, telefone.tipo.id, registro.nome.id),
                    )
                    telefone.id = cur.lastrowid
                else:
                    cur.execute(
                        """update telefones set número=?,
                                          id_tipo=?, id_nome=?
                                          where id = ?""",
                        (
                            telefone.número,
                            telefone.tipo.id,
                            registro.nome.id,
                            telefone.id,
                        ),
                    )
            for apagado in registro.telefones.apagados:
                cur.execute("delete from telefones where id = ?", (apagado,))
            self.conexao.commit()
            registro.telefones.limpa()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()

    def apaga(self, registro):
        """_summary_

        Args:
            registro (_type_): _description_
        """
        try:
            cur = self.conexao.cursor()
            cur.execute("delete from telefones where id_nome = ?", (registro.nome.id,))
            cur.execute("delete from nomes where id = ?", (registro.nome.id,))
            self.conexao.commit()
        except:
            self.conexao.rollback()
            raise
        finally:
            cur.close()


class Menu:
    """_summary_"""

    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adiciona_opcao(self, nome, funcao):
        """_summary_

        Args:
            nome (_type_): _description_
            funcao (_type_): _description_
        """
        self.opcoes.append([nome, funcao])

    def exibe(self):
        """_summary_"""
        print("====")
        print("Menu")
        print("====\n")
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i}] - {opcao[0]}")
        print()

    def execute(self):
        """_summary_"""
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opção: ", 0, len(self.opcoes) - 1
            )
            if escolha == 0:
                break
            self.opcoes[escolha][1]()


class AppAgenda:
    """_summary_

    Returns:
        _type_: _description_
    """

    @staticmethod
    def pede_nome():
        """_summary_

        Returns:
            _type_: _description_
        """
        return input("Nome: ")

    @staticmethod
    def pede_telefone():
        """_summary_

        Returns:
            _type_: _description_
        """
        return input("Telefone: ")

    @staticmethod
    def mostra_dados(dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        print(f"Nome: {dados.nome}")
        for telefone in dados.telefones:
            print(f"Telefone: {telefone}")
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        print(f"Nome: {dados.nome}")
        for i, telefone in enumerate(dados.telefones):
            print(f"{i} - Telefone: {telefone}")
        print()

    def __init__(self, banco):
        self.agenda = DBAgenda(banco)
        self.menu = Menu()
        self.menu.adiciona_opcao("Novo", self.novo)
        self.menu.adiciona_opcao("Altera", self.altera)
        self.menu.adiciona_opcao("Apaga", self.apaga)
        self.menu.adiciona_opcao("Lista", self.lista)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrao=None):
        """_summary_

        Returns:
            _type_: _description_
        """
        for i, tipo in enumerate(self.agenda.tipos_telefone):
            print(f" {i} - {tipo} ", end=None)
        tipo = valida_faixa_inteiro(
            "Tipo: ", 0, len(self.agenda.tipos_telefone) - 1, padrao
        )
        return self.agenda.tipos_telefone[tipo]

    def pesquisa(self, nome):
        """_summary_

        Args:
            nome (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(nome, str):  # type(nome) == str:
            nome = DBNome(nome)
        dado = self.agenda.pesquisa_nome(nome)
        return dado

    def novo(self):
        """_summary_"""
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = DBNome(novo)
        if self.pesquisa(nome) is not None:
            print("Nome já existe!")
            return
        registro = DBDadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.novo(registro)

    def apaga(self):
        """_summary_"""
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        nome = self.pesquisa(nome)
        if nome is not None:
            self.agenda.apaga(nome)
        else:
            print("Nome não encontrado.")

    def altera(self):
        """_summary_"""
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        nome = self.pesquisa(nome)
        if nome is not None:
            print("\nEncontrado:\n")
            AppAgenda.mostra_dados(nome)
            print("Digite enter caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                nome.nome.nome = novo
            self.menu_telefones(nome)
            self.agenda.atualiza(nome)
        else:
            print("Nome não encontrado!")

    def menu_telefones(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        while True:
            print("\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0:
                print("\n[A] - alterar\n[D] - apagar\n", end="")
            print("[N] - novo\n[S] - sair\n")
            operação = input("Escolha uma operação: ")
            operação = operação.lower()
            if operação not in ["a", "d", "n", "s"]:
                print("Operação inválida. Digite A, D, N ou S")
                continue
            if operação == "a" and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operação == "d" and len(dados.telefones) > 0:
                self.apaga_telefone(dados)
            elif operação == "n":
                self.novo_telefone(dados)
            elif operação == "s":
                break

    def novo_telefone(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisa_telefone(telefone) is not None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(DBTelefone(telefone, tipo))

    def apaga_telefone(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        posicao = valida_faixa_inteiro_ou_branco(
            "Digite a posição do número a apagar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if posicao is None:
            return
        dados.telefones.remove(dados.telefones[posicao])

    def altera_telefones(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        posicao = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a alterar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if posicao is None:
            return
        telefone = dados.telefones[posicao]
        print(f"Telefone: {telefone}")
        print("Digite enter caso não queira alterar o número")
        novotelefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novotelefone):
            telefone.número = novotelefone
        print("Digite enter caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tipos_telefone.pesquisa(telefone.tipo)
        )

    def lista(self):
        """_summary_"""
        print("\nAgenda")
        print("-" * 60)
        for entrada in self.agenda.lista():
            AppAgenda.mostra_dados(entrada)
        print("-" * 60)

    def execute(self):
        """_summary_"""
        self.menu.execute()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = AppAgenda(sys.argv[1])
        app.execute()
    else:
        print("Erro: nome do banco de dados não informado")
        print("      agenda.py nome_do_banco")
