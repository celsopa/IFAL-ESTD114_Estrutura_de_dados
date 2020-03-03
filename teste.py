def soma_ateh(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + soma_ateh(n-1)

print(soma_ateh(5))