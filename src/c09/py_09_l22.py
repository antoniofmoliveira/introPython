"""
Listagem 9.22 – Obtenção das horas em Python
"""
import time

agora = time.time()
print(agora)
print(time.ctime(agora))
agora2 = time.localtime()
print(agora2)
print(time.gmtime(agora))

agora3 = time.time()
time.sleep(2)
agora4 = time.time()
print(agora4-agora3)
print(time.ctime(f"{agora4-agora3:MS}"))
