"""
Listagem 4.8 – Categoria x preço, usando elif
"""
categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    PRECO = 10
elif categoria == 2:
    PRECO = 18
elif categoria == 3:
    PRECO = 23
elif categoria == 4:
    PRECO = 26
elif categoria == 5:
    PRECO = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    PRECO = 0
print(f"O preço do produto é: R$ {PRECO:6.2f}.")
