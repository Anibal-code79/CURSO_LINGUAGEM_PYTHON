#ORDENANDO UMA LISTA ATRAVES DE UMA COMPARACAO
numeros = []
troca= True
limite=int(input("Ola, quantos numeros voce precisa baralha-los: "))

for i in range(limite):
    valor=int(input(f"Digite o numero {i+1}: ",))
    numeros.append(valor)
    

while troca:
    troca= False
    for i in range(len(numeros)-1):
        if numeros[i]>numeros[i+1]:
            troca= True
            numeros[i], numeros[i+1]=numeros[i+1], numeros[i]

print("Lista em ordem crescrente: ", numeros)
print(
    """
    ==============================================
    Porem hoje em dia no python existem mecanismos 
    mais validos para tornar isso facil com
    o uso do variavel.sort().
    ==============================================
    """
)