"""
Listagem 10.13 – Classe ListaÚnica (listaunica.py)
"""


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
