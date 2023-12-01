"""
Listagem 5.10 - Contagem de questões corretas
"""
PONTOS = 0
QUESTAO = 1
while QUESTAO <= 3:
    resposta = input(f"Resposta da questão {QUESTAO:d}: ")
    if QUESTAO == 1 and resposta == "b":
        PONTOS = PONTOS + 1
    if QUESTAO == 2 and resposta == "a":
        PONTOS = PONTOS + 1
    if QUESTAO == 3 and resposta == "d":
        PONTOS = PONTOS + 1
    QUESTAO += 1
print(f"O aluno fez {PONTOS:d} ponto(s).")
