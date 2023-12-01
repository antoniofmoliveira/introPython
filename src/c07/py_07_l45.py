"""
Listagem 7.45 – Jogo da forca
"""
palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
ERROS = 0
while True:
    SENHA = ""
    for letra in palavra:
        SENHA += letra if letra in acertos else "."
    print(SENHA)
    if SENHA == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    # else:
    digitadas += tentativa
    if tentativa in palavra:
        acertos += tentativa
    else:
        ERROS += 1
        print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if ERROS >= 1 else "X")
    LINHA2 = ""
    if ERROS == 2:
        LINHA2 = "  |  "
    elif ERROS == 3:
        LINHA2 = " /|  "
    elif ERROS >= 4:
        LINHA2 = " /|\\ "
    print(f"X{LINHA2:s}")
    LINHA3 = ""
    if ERROS == 5:
        LINHA3 += " /   "
    elif ERROS >= 6:
        LINHA3 += " / \\ "
    print(f"X{LINHA3:s}")
    print("X\n===========")
    if ERROS == 6:
        print("Enforcado!")
        break
