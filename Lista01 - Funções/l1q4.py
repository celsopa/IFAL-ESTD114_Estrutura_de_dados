# 4. Escreva uma função compare(a, b) que recebe dois números a e b como parâmetro e retorna 1 se a > b, 0 se a == b, e -1
# se a < b.


def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


print(compare(8, 2))  # 1
print(compare(5, 5))  # 0
print(compare(1, 5))  # -1
