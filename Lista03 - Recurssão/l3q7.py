# 7. Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.
# O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15


def fatorial_duplo(n):
    if n < 2:
        return 1
    if n % 2 == 1:
        return n * fatorial_duplo(n-1)
    else:
        return fatorial_duplo(n-1)


print(fatorial_duplo(5))  # 15
print(fatorial_duplo(9))  # 945
