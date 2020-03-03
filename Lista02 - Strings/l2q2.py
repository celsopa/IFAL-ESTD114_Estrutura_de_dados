# 2. Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de palavras de um
# texto. Escreva um programa que determine o número de palavras de um texto dado.
# https://www.thehuxley.com/problem/1008?locale=pt_BR - Contar palavras


def contar_palavras(text):
    num_palavras = 0
    anterior = " "
    for x in text:
        if x == " " and anterior != " ":
            num_palavras += 1
        anterior = x
    if anterior != " ":
        num_palavras += 1
    return num_palavras


print(contar_palavras("A dama admirou o rim da amada"))  # 6
print(contar_palavras("Sairam      o tio e oito marias       "))  # 7
