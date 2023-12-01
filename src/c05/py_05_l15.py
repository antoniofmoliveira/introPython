"""
Listagem 5.15 - Impressão de tabuadas
"""
TABUADA = 1
while TABUADA <= 10:
    NUMERO = 1
    while NUMERO <= 10:
        print(f"{TABUADA:d} x {NUMERO:d} = {(TABUADA * NUMERO):d}.")
        NUMERO += 1
    TABUADA += 1
