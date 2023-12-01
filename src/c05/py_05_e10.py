"""
Exercício 5.10 Modifique o programa da listagem 5.10 para que aceite respostas
com letras maiúsculas e minúsculas em todas as questões.
"""
PONTOS = 0
QUESTAO = 1
while QUESTAO <= 3:
    resposta = input(f"Resposta da questão {QUESTAO:d}: ")
    if QUESTAO == 1 and (resposta == "b" or resposta == "B"):
        PONTOS = PONTOS + 1
    if QUESTAO == 2 and (resposta == "a" or resposta == "A"):
        PONTOS = PONTOS + 1
    if QUESTAO == 3 and (resposta == "d" or resposta == "D"):
        PONTOS = PONTOS + 1
    QUESTAO += 1
print(f"O aluno fez {PONTOS:d} ponto(s).")
