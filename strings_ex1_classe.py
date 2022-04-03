class Comparador:

    def __init__(self,string_1,string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def exibe_conteudo_string(self):

        print(f'Primeira string: {self.string_1}')
        print(f'Segunda string: {self.string_2}')

    def __len__(self):
        print(f'Tamanho da string 1: {len(self.string_1)} caracteres')
        print(f'Tamanho da string 2: {len(self.string_2)} caracteres')

    def comparador_de_strings(self):

        if self.string_1 == self.string_2:
            print("As duas strings possuem o mesmo conteúdo!")
        else:
            print("As duas strings possuem conteúdo diferente!")

    def comparador_de_tamanho_string(self):

        if len(self.string_1) == len(self.string_2):
            print("As strings possuem o mesmo tamanho!")
        else:
            print("As duas strings são de tamanhos diferentes!")


#VERIFICAÇÃO

strings = Comparador("Brasil Hexa 2006","Brasil! Hexa 2006")
strings.exibe_conteudo_string()
strings.__len__()
strings.comparador_de_strings()
strings.comparador_de_tamanho_string()

strings_2 = Comparador("Brasil Hexa 2006","Brasil Hexa 2006")
strings_2.exibe_conteudo_string()
strings_2.__len__()
strings_2.comparador_de_strings()
strings_2.comparador_de_tamanho_string()