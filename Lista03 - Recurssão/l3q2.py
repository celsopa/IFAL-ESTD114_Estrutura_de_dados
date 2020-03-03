# 2. Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"


def inverter(n):
    if n == '':
        return n
    else:
        return n[-1] + inverter(n[:-1])


print(inverter("Python"))  # nohtyP
print(inverter("amarelo"))  # olerama
print(inverter("Brasil"))  # lisarB
