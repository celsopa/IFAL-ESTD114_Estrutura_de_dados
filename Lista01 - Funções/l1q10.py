# 10. Faça uma função eh_data_valida(dia, mes, ano) que recebe como parâmetro três valores, representando dia, mês e ano.
# Essa função deve retornar True se os valores formarem uma data válida, e False caso contrário
# https://www.thehuxley.com/problem/1113?locale=pt_BR



def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    if ano % 400 == 0:
        return True
    return False


def eh_data_valida(dia, mes, ano):
    if mes < 1 or mes > 12 or dia < 0 or dia > 31:
        return False
    elif bissexto(ano):
        if mes == 2:
            if dia > 29:
                return False
        elif mes in [2, 4, 6, 9, 11]:
            if dia > 30:
                return False
    return True


print(eh_data_valida(29, 2, 2020))  # True
print(eh_data_valida(31, 4, 2020))  # False
