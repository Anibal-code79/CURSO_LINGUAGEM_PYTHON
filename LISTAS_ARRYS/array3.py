frutas=["Banana", "Manca", "Laranja", "Uva"]

#ADICIONANDO NA ULTIMA POSICAO DA LISTA
print("As frutas sao: ",frutas)
frutas.append("Jambalao")
print("As frutas agora sao: ",frutas)

#ADICIONANDO INDICANDO A POSICAO NA LISTA
frutas.insert(3,"Maracuja")
print("As frutas agora sao: ", frutas)

#ELIMINANDO UM VALOR NA LISTA
del frutas[4]
print("As frutas agora sao: ", frutas)