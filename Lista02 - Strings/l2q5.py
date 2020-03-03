# 5. As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de um livro texto, etc., exigem que o
# nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
# sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um
# programa que receba um nome e o escreva no formato de bibliografia.


def nome_bio(nomecompleto):
    nome = ""
    lista_nomes = []
    resultado = ""
    i = 0
    for x in nomecompleto:
        if x != " ":
            nome += x
        elif x == " ":
            lista_nomes.append(nome)
            nome = ""
    else:
        lista_nomes.append(nome)
    resultado += lista_nomes[-1] + ", "
    while True:
        if lista_nomes[i] == lista_nomes[-1]:
            break
        resultado += lista_nomes[i][0]+"."
        if lista_nomes[i+1] != lista_nomes[-1]:
            resultado += " "
        i += 1
    return resultado


print(nome_bio("Antônio Carlos Jobim"))  # Jobim, A. C.
print(nome_bio("Andrew Stuart Tanenbaum"))  # Tanenbaum, A. S.
print(nome_bio("William Stallings"))  # Stallings, W.
