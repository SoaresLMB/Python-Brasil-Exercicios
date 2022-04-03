# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self,t_lado):
        self.lado = t_lado

    def area(self):
        return self.lado**2

    @property
    def tamanho_lado(self):
        return self.lado

    @tamanho_lado.setter
    def tamanho_lado(self,t_lado):
        self.lado = t_lado



