"""
Listagem 6.53 – Exemplo de dicionário com estoque e operações de venda
"""
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
TOTAL = 0
print("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao
    PRECO = estoque[produto][1]
    CUSTO = PRECO * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {PRECO:6.2f} = {CUSTO:6.2f}")
    estoque[produto][0] -= quantidade
    TOTAL += CUSTO
    print(f" Custo total: {TOTAL:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
