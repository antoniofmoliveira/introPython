"""
Exercício 6.18 Escreva um programa que gere um dicionário, onde cada chave seja
um caractere, e seu valor seja o número desse caractere encontrado em uma
frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}
"""
frase = input("Digite uma frase: ")
contagem = {}
for e in frase:
    if e != " ":
        if e in contagem:
            contagem[e] += 1
        else:
            contagem[e] = 1
print(contagem)
