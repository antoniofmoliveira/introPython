"""
Listagem 7.30 – Limitação do tamanho de impressão dos parâmetros
Listagem 7.31 – Especificação de espaços à esquerda ou à direita
Listagem 7.32 – Centralização
Listagem 7.33 – Especificação de espaços à esquerda ou à direita
"""

print(f"{'123':10} {'456'}")
print(f"{'123':>10} {'456'}")
print(f"{'123':<10} {'456'}")
print(f"{123:10} {456}")
print(f"{123:>10} {456}")
print(f"{123:<10} {456}")

print(f"X{'123':10}X")
print(f"X{123:10}X")
print(f"X{'123':^10}X")
print(f"X{123:^10}X")

print(f"X{123:.<10}X")
print(f"X{123:!>10}X")
print(f"X{123:*^10}X")

print(f"X{'123456789012345':10}X")
print(f"X{123456789012345:10}X")
