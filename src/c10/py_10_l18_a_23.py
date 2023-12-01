"""
Listagem 10.18 – A classe TipoTelefone
"""
import sys
import pickle
from functools import total_ordering


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

    Returns:
        _type_: _description_
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

    def indicevalido(self, indice):
        """_summary_

        Args:
            i (_type_): _description_

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
        if not isinstance(elem, self.elem_class):  # type(elem) != self.elem_class:
            raise TypeError("Tipo inválido")

    def ordena(self, chave=None):
        """_summary_

        Args:
            chave (_type_, optional): _description_. Defaults to None.
        """
        self.lista.sort(key=chave)


@total_ordering
class Nome:
    """_summary_"""

    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return (
            f"<Classe {type(self).__name__} em 0x{id(self):x} "
            + f"Nome: {self.__nome} Chave: {self.__chave}>"
        )

    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
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
        if valor is None or not valor.strip():
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


@total_ordering
class TipoTelefone:
    """_summary_"""

    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"({self.tipo})"

    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo

    def __lt__(self, outro):
        return self.tipo < outro.tipo


# Listagem 10.19 – A classe Telefone


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
        return self.numero == outro.numero and (
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
        if valor is None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__numero = valor


# Listagem 10.20 – Classe DadoAgenda

class Telefones(ListaUnica):
    """_summary_

    Args:
        ListaUnica (_type_): _description_
    """

    def __init__(self):
        super().__init__(Telefone)


class DadoAgenda:
    """_summary_"""

    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):  # type(valor) != Nome:
            raise TypeError("nome deve ser uma instância da classe Nome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        """_summary_

        Args:
            telefone (_type_): _description_

        Returns:
            _type_: _description_
        """
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        # else:
        return self.telefones[posicao]


# Listagem 10.21 – Listagem parcial do programa da agenda
class TiposTelefone(ListaUnica):
    """_summary_

    Args:
        ListaUnica (_type_): _description_
    """

    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaUnica):
    """_summary_

    Args:
        ListaUnica (_type_): _description_
    """

    def __init__(self):
        super().__init__(DadoAgenda)
        self.tipos_telefone = TiposTelefone()

    def adiciona_tipo(self, tipo):
        """_summary_

        Args:
            tipo (_type_): _description_
        """
        self.tipos_telefone.adiciona(TipoTelefone(tipo))

    def pesquisa_nome(self, nome):
        """_summary_

        Args:
            nome (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(nome, str):  # type(nome) == str:
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        # else:
        return None

    def ordena(self, chave=None):
        """_summary_"""
        super().ordena(lambda dado: str(dado.nome))


# Listagem 10.22 – Listagem parcial da agenda: classe Menu
class Menu:
    """_summary_"""

    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adiciona_opcao(self, nome, funcao):
        """_summary_"""
        self.opcoes.append([nome, funcao])

    def exibe(self):
        """_summary_"""
        print("====")
        print("Menu")
        print("====\n")
        for i, opção in enumerate(self.opcoes):
            print(f"[{i}] - {opção[0]}")
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

    @staticmethod
    def pede_nome_arquivo():
        """_summary_

        Returns:
            _type_: _description_
        """
        return input("Nome do arquivo: ")

    def __init__(self):
        self.agenda = Agenda()
        self.agenda.adiciona_tipo("Celular")
        self.agenda.adiciona_tipo("Residência")
        self.agenda.adiciona_tipo("Trabalho")
        self.agenda.adiciona_tipo("Fax")
        self.menu = Menu()
        self.menu.adiciona_opcao("Novo", self.novo)
        self.menu.adiciona_opcao("Altera", self.altera)
        self.menu.adiciona_opcao("Apaga", self.apaga)
        self.menu.adiciona_opcao("Lista", self.lista)
        self.menu.adiciona_opcao("Grava", self.grava)
        self.menu.adiciona_opcao("Lê", self.carrega)
        self.menu.adiciona_opcao("Ordena", self.ordena)
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
        dado = self.agenda.pesquisa_nome(nome)
        return dado

    def novo(self):
        """_summary_"""
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = Nome(novo)
        if self.pesquisa(nome) is not None:
            print("Nome já existe!")
            return
        registro = DadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.adiciona(registro)

    def apaga(self):
        """_summary_"""
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a apagar")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        registro = self.pesquisa(nome)
        if registro is not None:
            self.agenda.remove(registro)
            print(
                f"Apagado. A agenda agora possui apenas: {len(self.agenda):d} registros"
            )
        else:
            print("Nome não encontrado.")

    def altera(self):
        """_summary_"""
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a alterar")
        nome = AppAgenda.pede_nome()
        registro = self.pesquisa(nome)
        if nulo_ou_vazio(nome):
            return
        if registro is not None:
            print("\nEncontrado:\n")
            AppAgenda.mostra_dados(registro)
            print("Digite enter caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                registro.nome = Nome(novo)
            self.menu_telefones(registro)
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
        dados.telefones.adiciona(Telefone(telefone, tipo))

    def apaga_telefone(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        tipo = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a apagar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if tipo is None:
            return
        dados.telefones.remove(dados.telefones[tipo])

    def altera_telefones(self, dados):
        """_summary_

        Args:
            dados (_type_): _description_
        """
        eh_valido = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a alterar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if eh_valido is None:
            return
        telefone = dados.telefones[eh_valido]
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
        for entrada in self.agenda:
            AppAgenda.mostra_dados(entrada)
        print("-" * 60)

    def carrega(self, nome_arquivo=None):
        """_summary_

        Args:
            nome_arquivo (_type_, optional): _description_. Defaults to None.
        """
        if nome_arquivo is None:
            nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            return
        with open(nome_arquivo, "rb") as arquivo:
            self.agenda = pickle.load(arquivo)
        self.ultimo_nome = nome_arquivo

    def ordena(self):
        """_summary_"""
        self.agenda.ordena()
        print("\nAgenda ordenada\n")

    def grava(self):
        """_summary_"""
        if self.ultimo_nome is not None:
            print(f"Último nome utilizado foi '{self.ultimo_nome:s}'")
            print("Digite enter caso queira utilizar o mesmo nome")
        nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            if self.ultimo_nome is not None:
                nome_arquivo = self.ultimo_nome
            else:
                return
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.agenda, arquivo)

    def execute(self):
        """_summary_"""
        self.menu.execute()


if __name__ == "__main__":
    app = AppAgenda()
    if len(sys.argv) > 1:
        app.carrega(sys.argv[1])
    app.execute()
