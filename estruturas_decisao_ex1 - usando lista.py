# Faça um Programa que peça dois números e imprima o maior deles.
# Utilizando Listas

numero = []
i = 0

while (i < 2):
    num_escolhido = float(input("Digite o {}º número".format(i+1)))
    numero.append(num_escolhido)
    i+=1

maior_numero = max(numero)
print("O maior número é o:",maior_numero)