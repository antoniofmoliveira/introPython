"""
Listagem 9.4 – Gravação de números pares e ímpares em arquivos diferentes
"""
# impares = open("ímpares.txt", "w")
# pares = open("pares.txt", "w")
# for n in range(0, 1000):
#     if n % 2 == 0:
#         pares.write("%d\n" % n)
#     else:
#         impares.write("%d\n" % n)
# impares.close()
# pares.close()

with open("ímpares.txt", "w", encoding="utf-8") as impares, open(
    "pares.txt", "w", encoding="utf-8"
) as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f"{n:d}\n")
        else:
            impares.write(f"{n:d}\n")
