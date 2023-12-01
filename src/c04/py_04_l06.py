"""
    Listagem 4.6 – Conta de telefone com três faixas de preço
"""
minutos = int(input("Quantos minutos você utilizou este mês:"))
if minutos < 200:
    PRECO = 0.20
else:
    if minutos < 400:
        PRECO = 0.18
    else:
        PRECO = 0.15
print(f"Você vai pagar este mês: R$ {(minutos * PRECO):6.2f}.")
