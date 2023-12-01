"""
Listagem 6.26 – Pesquisa usando for
"""
L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar:"))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")
