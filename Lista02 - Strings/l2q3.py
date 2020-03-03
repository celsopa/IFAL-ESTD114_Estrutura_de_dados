# 3. Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. Exemplo: Se a string digitada
# for "José da Silva", deverá ser impresso na tela a substring "Silva".
# https://www.thehuxley.com/problem/248?locale=pt_BR - Última palavra de uma frase


def ultima_palavra(texto):
    i = 0
    anterior = " "
    ind_esp = 0
    for x in texto:
        if x == " " and anterior != " ":
            ind_esp = i
        i += 1
        anterior = x
    return texto[ind_esp+1:]


print(ultima_palavra("José da Silva"))  # Silva
print(ultima_palavra("Desenvolva seu algoritmo para os problemas abaixo"))  # abaixo
