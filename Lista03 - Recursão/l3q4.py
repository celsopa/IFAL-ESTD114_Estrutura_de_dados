# 4. Escreva uma função recursiva que receba um número inteiro positivo N e
# imprima todos os números naturais de 0 até N em ordem crescente.


def contar(n):
    if n <= 0:
        print(0, end=" ")
    else:
        contar(n-1)
        print(n, end=" ")


contar(7)  # 0 1 2 3 4 5 6 7
print()  # pula linha
contar(20)  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
