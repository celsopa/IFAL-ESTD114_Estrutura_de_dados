# 5. Escreva uma função recursiva que receba um número inteiro positivo N e
# imprima todos os números naturais de 0 até N em ordem decrescente.


def contar(n):
    if n <= 0:
        print(0)
    else:
        print(n, end=" ")
        contar(n-1)


contar(5)  # 5 4 3 2 1 0
contar(11)  # 11 10 9 8 7 6 5 4 3 2 1 0
