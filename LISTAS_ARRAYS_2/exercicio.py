numeros=[]
limite=int(input("Quantos numeros pretendes digitar: "))
igual= True 

for i in range(limite):
    valor=input(f"Digite o numero {i + 1} que deseja cadastrar na tua lista: ")
    numeros.append(valor)

for i in range(len(numeros)-1):
    igual=False 
    if numeros[i]==numeros[i+1]:
        igual=True
        del numeros[i]

print("Os numeros existentes sem duplicacao: ", numeros)
    