# 7. Faça uma função dia_da_semana(dia) que recebe como parâmetro um número e retorna o dia correspondente da
# semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve retornar valor inválido.
# https://www.thehuxley.com/problem/1311?locale=pt_BR


def dia_da_semana(dia):
    dias = {1: "domingo",
            2: "segunda",
            3: "terça",
            4: "quarta",
            5: "quinta",
            6: "sexta",
            7: "sábado"}
    return dias[dia]


print(dia_da_semana(1))  # domingo
print(dia_da_semana(3))  # terça
