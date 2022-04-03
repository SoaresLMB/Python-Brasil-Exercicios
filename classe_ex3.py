#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe.
#Ele deve pedir ao usuário que informe as medidas de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,nova_base):
        self.__base = nova_base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,nova_altura):
        self.__altura = nova_altura

    def area(self):
        area = self.__altura * self.__base
        return area

    def perimetro(self):
        perimetro = 2*self.__base + 2*self.__altura
        return perimetro





