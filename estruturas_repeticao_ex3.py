#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';#Salário: maior que zero;

def nome (nome):
    if len(nome) >= 3:
        print(nome)
    else:
        print( "O nome deve ter mais que 3 caracteres")

nome_1 = input("NOME:")
nome(nome_1)

#idade = input("IDADE:")
#sexo = input('SEXO:')
#estado_civil = input("ESTADO CIVIL:")

nome(nome_1)


#parar = False

#while not parar:


    #cont = int(input("Digite 1 para outros cadastro ou 2 para parar"))

    #if cont == 1:
        #parar = False
    #else:
     #   parar = True