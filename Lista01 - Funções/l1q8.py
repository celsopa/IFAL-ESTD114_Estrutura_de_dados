# 8. Faça uma função hipotenusa(cateto1, cateto2) que retorna o comprimento da hipotenusa de um triângulo retângulo dados
# os comprimentos dos dois lados como parâmetros.
# https://www.thehuxley.com/problem/702?locale=pt_BR


def hipotenusa(cateto1, cateto2):
    hipotenusa = ((cateto1*cateto1) + (cateto2*cateto2))**(1/2)
    return hipotenusa


print(hipotenusa(3, 4))  # 5.0
print(hipotenusa(8, 15))  # 17.0
