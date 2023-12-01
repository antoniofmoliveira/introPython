"""Listagem 4.7 – Categoria x preço
"""
categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    PRECO = 10
else:
    if categoria == 2:
        PRECO = 18
    else:
        if categoria == 3:
            PRECO = 23
        else:
            if categoria == 4:
                PRECO = 26
            else:
                if categoria == 5:
                    PRECO = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    PRECO = 0
print(f"O preço do produto é: R$ {PRECO:6.2f}.")
