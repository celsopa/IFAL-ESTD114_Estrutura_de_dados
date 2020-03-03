# 1. Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1


def fatorial(n):
    if n == 1:
        return n
    else:
        return n * fatorial(n-1)


print(fatorial(4))  # 24
print(fatorial(5))  # 120
print(fatorial(6))  # 720
