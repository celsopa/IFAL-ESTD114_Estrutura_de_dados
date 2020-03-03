# 3. Faça uma função par_ou_impar(numero) que recebe um número inteiro e retorna “par” ou “impar”.


def par_ou_impar(n):
    if n % 2 == 1:
        return "impar"
    else:
        return "par"


print(par_ou_impar(12))  # par
print(par_ou_impar(99))  # impar
