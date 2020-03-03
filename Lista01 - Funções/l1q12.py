# 12. Faça uma função eh_primo(numero) que recebe como parâmetro um número inteiro e retorna True se ele é um número
# primo e False caso contrário. Um número é primo quando ele é divisível somente por um e por ele mesmo.


def eh_primo(numero):
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    else:
        return True


print(eh_primo(10))