"""
Listagem 8.43 – Utilizando a função type em um programa
"""
import types


def diz_o_tipo(algo):
    """_summary_

    Args:
        algo (_type_): _description_

    Returns:
        _type_: _description_
    """
    tipo = type(algo)
    if tipo == str:
        return "String"
    if tipo == list:
        return "Lista"
    if tipo == dict:
        return "Dicionário"
    if tipo == int:
        return "Número inteiro"
    if tipo == float:
        return "Número decimal"
    if isinstance(tipo, types.FunctionType):
        return "Função"
    if isinstance(tipo, types.BuiltinFunctionType):
        return "Função interna"
    return str(tipo)


print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1, 2, 3]))
print(diz_o_tipo({"a": 1, "b": 50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))
