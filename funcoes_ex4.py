#Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verif (i):
     if i > 0:
         return "P"
     else:
         return "N"

#VERIFICAÇÃO:
num = verif(-3)
print(num)

num2 = verif(7)
print(num2)

num3 = verif(0)
print (num3)