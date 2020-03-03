# 6. Faça uma função maior_de_3(num1, num2, num3)que, dados três números, retorna o maior deles.


def maior_de_3(num1, num2, num3):
    maior_num = num1
    if num2 > maior_num:
        maior_num = num2
    if num3 > maior_num:
        maior_num = num3
    return maior_num


print(maior_de_3(9, 8, 7))  # 9
print(maior_de_3(1, 5, 2))  # 5
print(maior_de_3(1, 2, 3))  # 3

