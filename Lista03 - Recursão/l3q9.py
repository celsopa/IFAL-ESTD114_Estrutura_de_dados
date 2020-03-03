# 9. O MDC de dois números inteiros é o maior número inteiro que divide ambos sem deixar resto.
# O MDC pode ser calculado através do algoritmo de Euclides. Abaixo uma função iterativa que calcula o MDC.
# Reescreva a função abaixo de forma recursiva.
# def MDC(a, b):
# while (b != 0):
# r = a % b
# a = b
# b = r
# return a


def mdc(a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return mdc(a, r)
    else:
        r = b % a
        if r == 0:
            return a
        else:
            return mdc(b, r)


print(mdc(70, 40))  # 10
print(mdc(40, 70))  # 10
print(mdc(16, 24))  # 8
