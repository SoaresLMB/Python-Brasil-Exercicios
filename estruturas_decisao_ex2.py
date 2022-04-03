# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

parar = False

while not parar:
    valor = float(input("Insira um valor númerico"))

    if (valor > 0):
        print("Valor positivo!")
    else:
        print("Valor negativo!")

    continuar_parar = int(input("Digite (1) para novo teste ou digite (2) para parar"))

    if (continuar_parar == 1):
        parar = False
    else:
        parar = True
        print("Teste encerrado!")
