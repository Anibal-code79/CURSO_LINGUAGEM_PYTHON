numeros=[1,2,3,4,5,6,7]

numeros[3]=int(input("Digite o numero para substituir o numero do meio: "))

del numeros[-1]
print(len(numeros))
print(numeros)