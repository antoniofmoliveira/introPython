"""
Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
saída do while.
"""
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
X = 0
while X < len(L):
    if L[X] == p:
        break
    X += 1
if X < len(L):
    print(f"{p:d} achado na posição {X:d}.")
else:
    print(f"{p:d} não encontrado.")
