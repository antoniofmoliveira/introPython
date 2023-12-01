"""
Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo
fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o
tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
Preço por tipo e faixa de consumo
Tipo        Faixa (kWh)     Preço
Residencial Até 500         R$ 0,40
            Acima de 500    R$ 0,65
Comercial   Até 1000        R$ 0,55
            Acima de 1000   R$ 0,60
Industrial  Até 5000        R$ 0,55
            Acima de 5000   R$ 0,60
"""
qtde_kwh = float(input("Digite o consumo em kWh: "))
tipo = input("Instalação (R)esidencial, (C)omercial ou (I)ndustrial: ")
if tipo == "R":
    if qtde_kwh <= 500:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.40:6.2f}.")
    else:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.65:6.2f}.")
elif tipo == "C":
    if qtde_kwh <= 1000:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.55:6.2f}.")
    else:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.60:6.2f}.")
elif tipo == "I":
    if qtde_kwh <= 5000:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.55:6.2f}.")
    else:
        print(f"O preço a pagar é de R$ {qtde_kwh*0.60:6.2f}.")
else:
    print("Tipo de instalação não reconhecida.")
