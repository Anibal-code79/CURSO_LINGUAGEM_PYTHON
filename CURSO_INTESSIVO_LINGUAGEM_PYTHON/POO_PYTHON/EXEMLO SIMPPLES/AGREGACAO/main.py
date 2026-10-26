from classes import CarinhoDeCompras, Produto

carrinho= CarinhoDeCompras()

p1= Produto("Camiseta", 50)
p2= Produto("Telefone", 10000)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

carrinho.lista_produtos()