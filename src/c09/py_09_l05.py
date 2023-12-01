"""
Listagem 9.5 – Filtragem exclusiva dos múltiplos de quatro
"""
# múltiplos4 = open("múltiplos de 4.txt", "w")
# pares = open("pares.txt")
# for l in pares.readlines():
#     if int(l) % 4 == 0:
#         múltiplos4.write(l)
# pares.close()
# múltiplos4.close()

with open("múltiplos de 4.txt", "w", encoding="utf-8") as multiplos4, open(
    "pares.txt", encoding="utf-8"
) as pares:
    for linhas in pares.readlines():
        if int(linhas) % 4 == 0:
            multiplos4.write(linhas)
