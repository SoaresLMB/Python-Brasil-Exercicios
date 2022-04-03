# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

parar = False

while not parar:
    sexo = input("digite M para masculino e F para feminino ").upper()
    if sexo == "M":
        print("Masculino")
        parar = True
    elif sexo == "F":
        print("Feminino")
        parar = True
    else:
        print("Letra inválida")
        parar = False




