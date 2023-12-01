"""
Exercício 6.5 Altere o programa da listagem 6.21 de forma a poder trabalhar com
vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três
atendimentos e, finalmente, a saída do programa.
"""
ULTIMO = 10
fila = list(range(1, ULTIMO + 1))
while True:
    print(f"\nExistem {len(fila):d} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacoes = input("Operação (F, A ou S) ou uma combinação delas:")
    X = 0
    SAIR = False
    while X < len(operacoes):
        operacao = operacoes[X]
        if operacao == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido:d} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ULTIMO += 1  # Incrementa o ticket do novo cliente
            fila.append(ULTIMO)
        elif operacao == "S":
            SAIR = True
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        X += 1
    if SAIR:
        print("Fila atual:", fila)
        break
