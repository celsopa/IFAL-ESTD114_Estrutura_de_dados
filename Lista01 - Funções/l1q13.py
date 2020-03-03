# 13. A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo
# subsequente corresponde a soma dos dois anteriores. Faça uma função Fibonacci(termo) que dado um número N
# representando o n-ésimo termo da sequencia de Fibonacci, retorna a soma desses termos. Exemplo: Fibonacci(7) = 20 ,
# pois os 7 primeiros termos da sequencia de Fibonacci são “0,1, 1, 2, 3, 5, 8” e sua soma é 20.


def fibonacci(n):
    t1 = 0
    t2 = 1
    soma = t1 + t2
    while n > 2:
        t_atual = t1 + t2
        print(t_atual)
        soma += t_atual
        n -= 1
        t1 = t2
        t2 = t_atual
    return soma


print(fibonacci(12))
