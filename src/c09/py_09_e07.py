"""
Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
terá no máximo 60 linhas. Adicione na última linha de cada página o número da
página atual e o nome do arquivo original.
"""
NUM_PAG = 1
NUM_LINHA = 0
NOME_ARQUIVO_ENTRADA = "entrada2.txt"
NOME_ARQUIVO_SAIDA = "saida.txt"
with open(NOME_ARQUIVO_ENTRADA, "r", encoding="utf-8") as entrada, open(
    NOME_ARQUIVO_SAIDA, "w", encoding="utf-8"
) as saida:
    for linha in entrada.readlines():
        temp_linha = linha
        while len(temp_linha) > 0:
            parte_linha = temp_linha[0:75]
            parte_linha = parte_linha.strip() + "\n"
            saida.write(parte_linha)
            temp_linha = temp_linha[76:]
            NUM_LINHA += 1
            if NUM_LINHA > 60:
                saida.write(f"\npágina: {NUM_PAG:d} - {NOME_ARQUIVO_SAIDA:s}\n\n")
                NUM_PAG += 1
                NUM_LINHA = 0
    if NUM_LINHA != 60:
        saida.write(f"\npágina: {NUM_PAG:d} - {NOME_ARQUIVO_SAIDA:s}\n")
        NUM_PAG += 1
        NUM_LINHA = 0
