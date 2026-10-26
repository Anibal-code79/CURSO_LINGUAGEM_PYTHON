class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

    def desconto(self, percentual):
        self.preco= self.preco - (self.preco* (percentual/100))

    #GETTER
    @property
    def preco(self):
        return self._preco
    
    #SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor= float(valor.replace("MZ", ""))
            
        self._preco= valor

