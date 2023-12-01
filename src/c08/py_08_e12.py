"""
Exercício 8.12 Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também passada como
parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e
falso em caso contrário.
"""


def estah_na_lista(texto, lista):
    """verifica se texto está na lista

    Args:
        texto (string): texto a ser procurado
        lista (string[]): lista a ser varrida

    Returns:
        boolean: True se texto estiver na lista
                 False se texto não estiver na lista
    """
    for elemento in lista:
        if texto == elemento:
            return True
    return False


print(estah_na_lista("quinto", ["primeiro", "terceiro", "quarto", "quinto"]))
print(estah_na_lista("Quinto", ["primeiro", "terceiro", "quarto", "quinto"]))
