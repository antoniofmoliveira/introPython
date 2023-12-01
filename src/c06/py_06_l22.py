"""
Listagem 6.22 – Pilha de pratos
"""
PRATO = 5
pilha = list(range(1, PRATO + 1))
while True:
    print(f"\nExistem {len(pilha):d} pratos na pilha")
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S):")
    if operacao == "D":
        if (len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado:d} lavado")
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E":
        PRATO += 1  # Novo prato
        pilha.append(PRATO)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")
