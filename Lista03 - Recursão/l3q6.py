# 6. Escreva uma função recursiva que calcule o Nésimo termo da sequencia de Fibonacci.
# A sequência de Fibonacci é 0, 1, 1, 2, 3, 5, 8, 13, 21,...


def termo_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return termo_fibonacci(n-1) + termo_fibonacci(n-2)


print(termo_fibonacci(9))  # 21
print(termo_fibonacci(5))  # 3

