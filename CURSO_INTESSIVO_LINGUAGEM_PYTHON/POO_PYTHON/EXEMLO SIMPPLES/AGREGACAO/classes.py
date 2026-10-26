class CarinhoDeCompras:
    def __init__(self):
        self.produtos= []
    
    def inseirir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somar_total(self):
        for produto in self.produtos:
            total+=produto.valor
        return total
    
class Produto:
    def __init__(self, nome, valor):
        self.nome= nome
        self.valor= valor