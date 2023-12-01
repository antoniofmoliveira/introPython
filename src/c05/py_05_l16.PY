"""
Listagem 5.16 - Impressão de tabuadas sem repetições aninhadas
"""
TABUADA = 1
NUMERO = 1
while TABUADA <= 10:
    print(f"{TABUADA:d} x {NUMERO:d} = {(TABUADA * NUMERO):d}.")
    NUMERO += 1
    if NUMERO == 11:
        NUMERO = 1
        TABUADA += 1
