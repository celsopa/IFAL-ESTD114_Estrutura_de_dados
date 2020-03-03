# 3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P.
# Por exemplo, a letra 'u' ocorre 2 vezes em "estrutura"


def conta_letra(letra, palavra):
    if palavra == "":
        return 0
    if letra == palavra[-1]:
        return 1 + conta_letra(letra, palavra[:-1])
    else:
        return conta_letra(letra, palavra[:-1])


print(conta_letra("a", "cagado"))

