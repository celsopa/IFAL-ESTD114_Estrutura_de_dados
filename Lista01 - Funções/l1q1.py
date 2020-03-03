# Faça uma função fatorial(n) que, dado um número N, calcule e retorne o fatorial de N. O fatorial de um número natural n,
# representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. Exemplos: 5! = 1 x 2 x 3 x 4 x 5 = 120
# 0! = 1
# https://www.thehuxley.com/problem/936?locale=pt_BR - Fatorial


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)


print(fatorial(4))  # 24
print(fatorial(5))  # 120
