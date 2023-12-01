"""
Listagem 6.42 – Impressão das compras
"""
produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
for e in compras:
    print(f"Produto: {e[0]:s}")
    print(f"Quantidade: {e[1]:d}")
    print(f"Preço: {e[2]:5.2f}")
