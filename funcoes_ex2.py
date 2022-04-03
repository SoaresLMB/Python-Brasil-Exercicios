# Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def sequencia_numerica(n):
    numero = 1
    nu_seq = []

    while numero <= n:

        nu_seq.append(numero)
        print(*nu_seq)
        numero +=1

#VERIFICAÇÃO:
sequencia_numerica(5)