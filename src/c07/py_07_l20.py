"""
Listagem 7.20 – Remoção de caracteres com strip, lstrip e rstrip
"""
S = "...///Olá///..."
print(S.lstrip("."))
print(S.rstrip("."))
print(S.strip("."))
print(S.strip("./"))
