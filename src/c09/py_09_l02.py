"""
Listagem 9.2 – Abrindo, lendo e fechando um arquivo
"""
# arquivo=open("números.txt","r")
with open("números.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
# arquivo.close()
