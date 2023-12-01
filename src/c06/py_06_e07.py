"""
Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(())        OK
()()(()())  OK
())         Erro
"""
expresssao = input("Digite a expressao com parênteses: ")
pilha = []
ESTOUROU_PILHA = False
X = 0
while X < len(expresssao):
    p = expresssao[X]
    if p == "(":
        pilha.extend("(")
    elif p == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            ESTOUROU_PILHA = True
            break
    X += 1
if len(pilha) == 0 and not ESTOUROU_PILHA:
    print("Parênteses estão balanceados.")
else:
    print("Parênteses NÃO estão balanceados.")
