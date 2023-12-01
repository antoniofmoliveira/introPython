"""
Listagem 8.37 – Adivinhando o número
Exercício 8.13 Altere o programa da listagem 8.37 de forma que o usuário tenha
três chances de acertar o número. O programa termina se o usuário acertar ou
errar três vezes.
"""
import random

alvo = random.randint(1, 10)
qtde_tentativas = 3
while qtde_tentativas > 0:
    chute = int(input("Escolha um número entre 1 e 10: "))
    if chute == alvo:
        print("Você acertou!")
        break
    qtde_tentativas -= 1
    if qtde_tentativas == 0:
        print("Você errou.")
        print(alvo)
    else:
        print(f"Tente novamente. Mais {qtde_tentativas:d} chance(s).")
