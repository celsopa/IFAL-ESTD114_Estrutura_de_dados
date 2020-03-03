# 11. Faça uma função soma_numeros(numero) que recebe como parâmetro um número N, calcula a soma de todos os números
# de 1 até ele e retorna o valor da soma. Exemplo: soma_numeros(7) = 28 , pois 1+2+3+4+5+6+7=28.


def soma_numeros(N):
    soma = 0
    count = 1
    while count <= N:
        soma += count
        count += 1
    return soma


print(soma_numeros(7))  # 28
print(soma_numeros(2))  # 3
print(soma_numeros(1))  # 1
