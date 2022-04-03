#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

parar = False
n= 0

while not parar:

    nome_usuario = (input("Insira seu nome:"))
    nome_usuario = nome_usuario.upper().strip()
    senha = (input("Cadastre sua senha"))
    senha = senha.upper().strip()

    if nome_usuario == senha:
        print("Sua senha não pode ser igual ao seu nome")
        parar = False
    else:
        print("Usuário cadastrado com sucesso")
        parar = True

    n+=1
