# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

parar = False

while not parar:

    raio = float(input(" Informe o raio do círculo em metros:"))
    area_circulo = math.pi*raio**2
    diametro_circulo = 2*raio
    perimetro = math.pi*diametro_circulo

    print("Área do círculo: {:.4f} m2, Diâmetro: {}m, Perimetro: {:.4f}m".format(area_circulo,diametro_circulo,perimetro))

    continuar_parar = int(input("Digite (1) para cálculo de novo círculo e (2) para encerrar."))

    if(continuar_parar==1):
        parar = False
    else:
        parar = True
        print("Programa Encerrado.")
