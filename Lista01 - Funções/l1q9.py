# 9. Faça uma função eh_bissexto(ano) que recebe um ano como parâmetro e retorna True se o ano for bissexto e False caso
# contrário
# https://www.thehuxley.com/problem/568?locale=pt_BR


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    if ano % 400 == 0:
        return True
    return False


print(bissexto(1988))  # True
print(bissexto(1900))  # False
print(bissexto(2036))  # True
