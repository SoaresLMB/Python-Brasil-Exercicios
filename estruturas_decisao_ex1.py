#  Faça um Programa que peça dois números e imprima o maior deles.

numero_um = float(input("digite um número"))
numero_dois = float(input("digite o outro número"))

if (numero_um > numero_dois):
    print("O maior número é o:",numero_um)
elif (numero_dois > numero_um):
    print("O maior número é o:",numero_dois)
else:
    print("os números são iguais")