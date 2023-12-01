"""_summary_
"""
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R$ {bonus:5.2f}")  # print("Bônus de R$ %5.2f" % bonus)
