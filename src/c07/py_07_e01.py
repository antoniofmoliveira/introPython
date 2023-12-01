"""
Exercício 7.1 Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1a string: AABBEFAATT
2a string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""
alvo = input("Digite string alvo: ")
termo = input("Digite termos a ser procurado: ")
pos = alvo.find(termo)
if pos > 0:
    print(f"{termo} encontrado na posição {pos:d} de {alvo}.")
else:
    print("Termo não encontrado.")
