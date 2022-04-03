#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

parar = False
n = 0

while not parar:
    nota = int(input("insira uma nota entre 0 e 10:"))

    if (nota > 0) and (nota < 11):
        print(f'Sua nota é {nota}.')
        parar = True
    else:
        print("Você deve inserir um valor entre 0 e 10")
        parar = False

    n+=1
