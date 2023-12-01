"""
Exercício 7.9 Modifique o programa para utilizar listas de strings para
desenhar o boneco da forca. Você pode utilizar uma lista para cada linha e
organizá-las em uma lista de listas. Em vez de controlar quando imprimir cada
parte, desenhe nessas listas, substituindo o elemento a desenhar.
"""
lista_de_palavras = [
    "Modifique",
    "jogo",
    "forca",
    "forma",
    "utilizar",
    "uma",
    "lista",
    "palavras",
    "inicio",
    "pergunte",
    "numero",
    "calcule",
    "indice",
    "palavra",
    "utilizar",
    "pela",
    "formula",
]
patibulo = ["X==:==", "X  :  ", "X", "X", "X", "X", "==========="]
semente = int(input("Digite um número:"))
indice = (semente * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice].lower().strip()
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
    if ERROS == 1:
        patibulo[2] = "X  O  "
    elif ERROS == 2:
        patibulo[3] = "X  |  "
    elif ERROS == 3:
        patibulo[3] = "X /|  "
    elif ERROS == 4:
        patibulo[3] = "X /|\\ "
    elif ERROS == 5:
        patibulo[4] = "X /   "
    elif ERROS == 6:
        patibulo[4] = "X / \\"
    for e in patibulo:
        print(e)
    if ERROS == 6:
        print(f"Enforcado! A palavra é '{palavra}'.")
        break
