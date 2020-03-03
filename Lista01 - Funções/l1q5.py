# 5. Faça uma função maior_de_2(num1, num2) que, dados dois números, retorna o maior deles.
# https://www.thehuxley.com/problem/1060?locale=pt_BR - Maior de 2


def maior_de_2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(maior_de_2(9, 3))  # 9
print(maior_de_2(2, 6))  # 6
print(maior_de_2(5, 5))  # 5
