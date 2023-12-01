"""
Listagem 6.21 – Simulação de uma fila de banco
"""
ULTIMO = 10
fila = list(range(1, ULTIMO + 1))
while True:
    print(f"\nExistem {len(fila):d} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
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
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
