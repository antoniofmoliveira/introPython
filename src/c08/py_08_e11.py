"""
Exercício 8.11 Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne
verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
e falso em caso contrário.
"""


def valida_texto(texto, minimo, maximo):
    """valido tamanho de um texto

    Args:
        texto (string): texto a ser validado
        minimo (int): tamanho mínimo aceito
        maximo (int): tamanho máximo aceito

    Returns:
        boolean: True se tamanho do texo estive entre minimo e maximo.
                 False se o tamanho texto menor que minimo ou maior que maximo
    """
    tamanho = len(texto)
    if tamanho < minimo or tamanho > maximo:
        return False
    return True


print(valida_texto("texto", 3, 6))
print(valida_texto("texto", 1, 4))
