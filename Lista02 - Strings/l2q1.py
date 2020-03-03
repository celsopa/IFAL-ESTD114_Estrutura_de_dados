# 1. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar é palíndroma.
# Escreva um programa que verifique se uma palavra dada é palíndroma.
# https://www.thehuxley.com/problem/1008?locale=pt_BR


def eh_palindromo(palavra):
    i = 1
    for x in palavra:
        if x != palavra[-i]:
            return False
        i += 1
    return True


print(eh_palindromo("raiar"))  # True
print(eh_palindromo("reviver"))  # True
print(eh_palindromo("roedor"))  # False