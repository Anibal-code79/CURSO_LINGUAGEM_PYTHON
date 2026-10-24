produtos=[]
print(
    """
     =========================================
    | Ola, seja bem vindo ao nosso sistema    |
    | de vendas online, escolhe quais sao os  |
    | produtos que voce deseja comprar.       |
     =========================================
    """
)
limite=int(input("Quantos produtos voce deseja comprar: "))
for i in range(limite):
    produto=input(f"Digite o produto {i + 1} que deseja adiquirir: ")
    produtos.append(produto)

print("Os produtos que deseja comparar aqui estao: ", produtos)
