"""
Listagem 9.1 – Abrindo, escrevendo e fechando um arquivo
"""
# arquivo=open("números.txt","w")
with open("números.txt", "w", encoding="utf-8") as arquivo:
    for linha in range(1, 101):
        arquivo.write(f"{linha:d}\n")
# arquivo.close()
