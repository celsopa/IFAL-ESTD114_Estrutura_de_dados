# 2. Faça uma função eh_par(numero) que recebe um número inteiro e retorna True (verdadeiro) se o número for par, False
# (falso) caso contrário.


def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(eh_par(3))  # False
print(eh_par(26))  # True