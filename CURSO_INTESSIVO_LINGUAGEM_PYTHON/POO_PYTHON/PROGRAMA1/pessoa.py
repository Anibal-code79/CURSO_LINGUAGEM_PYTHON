from random import randint
#CRIACAO DE UMA CLASSE COMO MOLDE PARA OBJECTOS
class Pessoa:
    def __init__(self, nome, idade, comendo=False):
        self.nome= nome
        self.idade= idade
        self.comendo= comendo
        
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} ja esta comendo")
            return

        print(f"{self.nome} esta comendo {alimento}")
        self.comendo= True

    def saudar(self, curso):
        if self.comendo:
             print("nao pode saudar enquanto esta comendo")
             return

        print(f"Ola {self.nome} seja bem vindo ao nosso curo de {curso}")
        self.comendo= True

            
    def parar_comer(self):
            if not self.comendo:
                print(f"{self.nome} nao esta comendo")
                return
            
            print(f"{self.nome} parrou de comer")
            self.comendo=True

    #METODO DA CLASSE COM O RETORNO DO OBJECTO
    @classmethod
    def criacao_objecto_classe(cls, nome, idade):
         return cls(nome, idade)

    #METODO ESTATICO NAO RECEBE PARAMETROS NEM DA CLASSE NEM DO OBJECTO
    #ESTE METODO DA CLASSE GERA ID DE FORMA ALEARTPORIA USANDO UMA BIBLIOTECA PYTHON 
    @staticmethod 
    def gera_id():
        rand= randint(1000, 19999)
        return rand
    