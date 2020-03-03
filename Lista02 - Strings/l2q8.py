# 8. Os editores de texto possuem um recurso que permite o usuário substituir uma palavra de um texto por outra palavra.
# Escreva um programa que realize esta ação numa frase dada.


def substituir_palavra(frase, nova, velha):
    lista = []
    anterior = " "
    palavra = ""
    nova_frase = ""
    qtd = 0
    i = 0
    for x in frase:
        if x != " ":
            palavra += x
        else:
            lista.append(palavra)
            qtd += 1
            palavra = ""
        anterior = x
    else:
        lista.append(palavra)
        qtd += 1
    while i < qtd:
        if lista[i] == velha:
            nova_frase += nova
        else:
            nova_frase += lista[i]
        if i != qtd - 1:
            nova_frase += " "
        i += 1

    return nova_frase


frase = "Levaremos um tempo para crescer, levaremos um tempo para amadurecer, levaremos um tempo para entender, levaremos um tempo para envelhecer, levaremos um tempo para morrer"
velha = "levaremos"
nova = "teremos"

print(substituir_palavra(frase, nova, velha))