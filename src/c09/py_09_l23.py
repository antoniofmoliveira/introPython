"""
Listagem 9.23 – Obtenção de data e hora por nome
"""
import time

agora = time.localtime()
print(f"Ano: {agora.tm_year:d}")
print(f"Mês: {agora.tm_mon:d}")
print(f"Dia: {agora.tm_mday:d}")
print(f"Hora: {agora.tm_hour:d}")
print(f"Minuto: {agora.tm_min:d}")
print(f"Segundo: {agora.tm_sec:d}")
print(f"Dia da semana: {agora.tm_wday:d}")
print(f"Dia no ano: {agora.tm_yday:d}")
print(f"Horário de verão: {agora.tm_isdst:d}")
