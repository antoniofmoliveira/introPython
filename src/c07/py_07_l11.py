"""
Listagem 7.11 – Pesquisa de strings, limitando o início ou o fim
"""
S = "um tigre, dois tigres, três tigres"
print(S.find("tigres"))
print(S.rfind("tigres"))
print(S.find("tigres", 7))  # início=7
print(S.find("tigres", 30))  # início=30
print(S.find("tigres", 0, 10))  # início=0 fim=10
