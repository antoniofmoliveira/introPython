"""
Listagem 7.36 – Zeros à esquerda
"""
print(f"{5:05}")

# Listagem 7.37 – Preenchimento com outros caracteres
print(f"{32:*=7}")

# Listagem 7.38 – Combinação de vários códigos de formatação
print(f"{123:*^10}")
print(f"{123:*<10}")
print(f"{123:*>10}")

# Listagem 7.39 – Separação de milhares
print(f"{7532:10,}")
print(f"{1500.31:10.5f}")
print(f"{150031:10,.5f}")

# Listagem 7.40 – Impressão de sinais de positivo e negativo
print(f"{5:+10} {-6:-10}")
print(f"{5:-10} {-6: 10}")
print(f"{5: 10} {-6:+10}")

# Listagem 7.41 – Formatação de inteiros
print(f"{5678:b}")
print(f"{65:c}")
print(f"{5678:o}")
print(f"{5678:x}")
print(f"{5678:X}")
