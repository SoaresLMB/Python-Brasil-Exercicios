#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

def executa(string_1,string_2):

    exibe_conteudo_string(string_1,string_2)
    exibe_tamanho_string(string_1,string_2)
    comparador_de_strings(string_1,string_2)
    comparador_de_tamanho_string(string_1,string_2)

def exibe_conteudo_string(string_1,string_2):

    print(f'Primeira string: {string_1}')
    print(f'Segunda string: {string_2}')

def exibe_tamanho_string(string_1,string_2):

    print(f'Tamanho da string 1: {len(string_1)} caracteres')
    print(f'Tamanho da string 2: {len(string_2)} caracteres')

def comparador_de_strings(string_1,string_2):


    if string_1 == string_2:
        print("As duas strings possuem o mesmo conteúdo!")
    else:
        print("As duas strings possuem conteúdo diferente!")

def comparador_de_tamanho_string(string_1,string_2):

    if len(string_1) == len(string_2):
        print("As strings possuem o mesmo tamanho!")
    else:
        print("As duas strings são de tamanhos diferentes!")

#VERIFICAÇÃO

executa("Brasil Hexa 2006","Brasil! Hexa 2006")

executa("Brasil Hexa 2006","Brasil Hexa 2006")