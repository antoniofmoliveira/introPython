"""
Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para
facilitar seu trabalho, considere o comando A para atendimento da fila 1;
e B, para atendimento da fila 2. O mesmo para a chegada de clientes:
F para fila 1; e G, para fila 2.
"""
ULTIMO_A = 10
ULTIMO_B = 10
fila_A = list(range(1, ULTIMO_A + 1))
fila_B = list(range(1, ULTIMO_B + 1))
while True:
    print(f"\nExistem {len(fila_A):d} clientes na fila A")
    print(f"\nExistem {len(fila_B):d} clientes na fila B")
    print("Fila A atual:", fila_A)
    print("Fila B atual:", fila_B)
    print("Digite F para adicionar um cliente ao fim da fila A,")
    print("ou A para realizar o atendimento da fila A.")
    print("Digite G para adicionar um cliente ao fim da fila B,")
    print("ou B para realizar o atendimento da fila B. S para sair.")
    operacoes = input("Operação (F, G, A, B ou S) ou uma combinação delas:")
    X = 0
    SAIR = False
    while X < len(operacoes):
        operacao = operacoes[X]
        if operacao == "A":
            if (len(fila_A)) > 0:
                atendido = fila_A.pop(0)
                print(f"Cliente {atendido:d} da fila A atendido")
            else:
                print("Fila A vazia! Ninguém para atender.")
        elif operacao == "B":
            if (len(fila_B)) > 0:
                atendido = fila_B.pop(0)
                print(f"Cliente {atendido:d} da fila B atendido")
            else:
                print("Fila B vazia! Ninguém para atender.")
        elif operacao == "F":
            ULTIMO_A += 1  # Incrementa o ticket do novo cliente na fila A
            fila_A.append(ULTIMO_A)
        elif operacao == "G":
            ULTIMO_B += 1  # Incrementa o ticket do novo cliente na fila B
            fila_B.append(ULTIMO_B)
        elif operacao == "S":
            SAIR = True
        else:
            print("Operação inválida! Digite apenas F, G, A, B ou S!")
        X += 1
    if SAIR:
        print("Fila A atual:", fila_A)
        print("Fila B atual:", fila_B)
        break
