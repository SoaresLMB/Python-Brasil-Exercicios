# Faça um Programa que peça dois números e imprima a soma.

numeros = []
i = 0

while (i < 2):
    numero = float(input("Digite o {}° número que deseja somar:".format(i+1)))
    numeros.append(numero)
    i += 1

soma = sum(numeros)

print("Resultado:",soma)