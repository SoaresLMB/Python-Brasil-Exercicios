#Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Bola:

    def __init__(self,cor,circunferencia,material):
        self.__circunferencia = circunferencia
        self.__material = material
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self,cor):
        self.__cor = cor










