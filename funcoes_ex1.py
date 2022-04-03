#Faça um programa para imprimir:
   # 1
   # 2   2
   # 3   3   3
   #.....
   # n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.



def sequencia_numerica(n):
    numero = 1

    while numero <= n:
        num_str = ((str(numero) + " ")*numero)
        numero +=1
        print(num_str)

#VERIFICAÇÃO:
sequencia_numerica(3)

