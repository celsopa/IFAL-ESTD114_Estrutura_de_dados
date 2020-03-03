# 4. As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
# sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria indicado por Andrade/Carlos. Escreva um
# programa que lê um nome e o escreve no formato acima.


def nome_padrao(nome):
    i = 0
    ind_esp = 0
    primeiro = ""
    anterior = " "
    for x in nome:
        if x != " ":
            primeiro += x
        elif x == " " and anterior != " ":
            break
        anterior = x
    for x in nome:
        if x == " " and anterior != " ":
            ind_esp = i
        i += 1
        anterior = x
    ultimo = nome[ind_esp + 1:]
    return ultimo+"/"+primeiro


print(nome_padrao("Carlos Drumond de Andrade"))  # Andrade/Carlos
print(nome_padrao("Celso Pereira de Araújo"))  # Araújo/Celso
