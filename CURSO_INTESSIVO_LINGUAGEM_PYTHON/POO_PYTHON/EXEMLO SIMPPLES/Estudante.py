class Estudante:
    escola= "Instituto Foco"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade= idade

    def apresentar(self):
        print(f"Ola {self.nome}")

    @property
    def gett(self):
        return  self.nome

    @idade.setter
    def idade(self, valor):
        if self.idade>18:
            self.idade= valor
        else: 
            print("menor de idade")


    @classmethod
    def mostrar_escola(cls):
        print(cls.escola)

    @staticmethod
    def validar_nota(nota):
        return 0<= nota <=20

estudante= Estudante("Anibal")
estudante.apresentar()
Estudante.mostrar_escola()
print(Estudante.validar_nota(15))