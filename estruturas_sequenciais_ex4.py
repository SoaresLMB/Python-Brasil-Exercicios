# Faça um Programa que peça as 4 notas bimestrais e mostre a média

import statistics

i = 0
nota_bimestre = []

while (i < 4):
    nota = float(input("Insira a nota do bimestre {}:".format(i+1)))
    nota_bimestre.append(nota)
    i += 1

media = statistics.mean(nota_bimestre)
print("Média:",media)

