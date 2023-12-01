"""
Listagem 10.14 – Classe Nome (nome.py)

Listagem 10.15 – Usando anotações (nome.py)

Listagem 10.16 – Classe Nome com propriedades (nome.py)

Listagem 10.17 – Chave como propriedade apenas para leitura (nome.py)
"""
from functools import total_ordering  # 10.15


@total_ordering
class Nome:
    """_summary_"""

    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        # self.chave = nome.strip().lower() # 10.14
        # self.chave = Nome.cria_chave(nome)  # 10.15 # 10.16 retira a linha

    def __str__(self):
        return self.nome

    def __repr__(self):
        return (
            f"<Classe {type(self).__name__} em 0x{id(self):x} "
            + f"Nome: {self.__nome} Chave: {self.__chave}>"  # 10.16
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
