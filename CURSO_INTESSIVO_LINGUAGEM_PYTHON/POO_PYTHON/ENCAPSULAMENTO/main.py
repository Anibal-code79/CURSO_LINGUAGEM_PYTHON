"""
QUANDO UM ATRIBUTO TEM UM _ NO COECO NAO E POSSIVEL ACEDELA FORA DA CLASSE 
POR EXEMPLO: self._dados= {}  PROPORCIONANDO A ESCONDER 

USA SE TAMBEM O __ PARA REFORRCAR O ACESSO A ATRIBUTO DE UMA CLASSE 


"""
class BasedeDados:
    def __init__(self):
        self.dados= {}

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.dados:
            self.dados["clientes"]= {id: nome}
        else: 
            self.dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados["clientes"].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados["clientes"][id]


bd= BasedeDados()
bd.inserir_cliente(1, "Anibal")
bd.inserir_cliente(2, "Mutevui")
bd.inserir_cliente(3, "Charton")

bd.apaga_cliente(3)
bd.lista_clientes()
