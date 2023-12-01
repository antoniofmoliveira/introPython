"""
Listagem 7.42 – O formato d e o formato n
"""
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
print(f"{5678:d}")
print(f"{5678:n}")

# Listagem 7.43 – Formatação de números decimais
print(f"{1579.543:f}")
print(f"{1579.543:n}")
