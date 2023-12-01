"""
Cálculo do Imposto de Renda
"""
salario = float(input("Digite o salário para cálculo do imposto: "))
BASE = salario
IMPOSTO = 0
if BASE > 3000:
    IMPOSTO = IMPOSTO + ((BASE - 3000) * 0.35)
    BASE = 3000
if BASE > 1000:
    IMPOSTO = IMPOSTO + ((BASE - 1000) * 0.20)
print(f"Salário: R$ {salario:6.2f} Imposto a pagar: R$ {IMPOSTO:6.2f}.")
