# 7. Escreva uma função que gere logins para usuários de um sistema de computação baseado na seguinte regra: o login é
# composto pelas letras iniciais do nome do usuário.


def gera_login(nomecompleto):
    login = ""
    anterior = " "
    for x in nomecompleto:
        if x != " " and anterior == " ":
            login += x
        anterior = x
    return login


print(gera_login("Celso Pereira de Araujo"))  # CPdA
print(gera_login("Antônio Carlos Jobim"))  # ACJ
print(gera_login("Andrew Stuart Tanenbaum"))  # AST
print(gera_login("William Stallings"))  # WS

