"""
Exercício 6.17 Altere o programa da listagem 6.53 de forma a solicitar ao
usuário o produto e a quantidade vendida. Verifique se o nome do produto
digitado existe no dicionário, e só então efetue a baixa em estoque.
"""
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
TOTAL = 0
print("Vendas:\n")
while True:
    produto = input("Informe produto: ")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Informe quantidade vendida: "))
        PRECO = estoque[produto][1]
        CUSTO = PRECO * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {PRECO:6.2f} = {CUSTO:6.2f}")
        estoque[produto][0] -= quantidade
        TOTAL += CUSTO
    else:
        print("Estoque inexistente.")
print(f" Custo total: {TOTAL:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
