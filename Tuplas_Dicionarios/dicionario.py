numeros_telefones= {
    "Anibal": 873044890,
    "Andre": 865282744,
    "Lina": 857988000
    }
#IMPRESSAO DE TODOS DADOS DO DICIONARIO
print(numeros_telefones)

#IMPRESSAO DE UM DOS ELEMENTOS
print(numeros_telefones["Anibal"])

#VERIFICAR SE UMA CHAVE FAZ PARTE DE UM DCIONARIO
if "Andre" in numeros_telefones:
    print("Sim ele faz parte da lista")
if "Beleza" not in numeros_telefones:
    print("Nao faz parte da lista")

#VERIFICAR O NUMERO DE CHAVES E VALORES QUE FAZEM PARTE DE UMA LISTA
print(len(numeros_telefones))

#METODO KEY PARA PRECORRER UM DICIONARIO
for key in numeros_telefones.keys():
    print(key, " -> ", numeros_telefones[key])

#MODIFICAR VALORES DE UM DICIONARIO
numeros_telefones["Anibal"]=857988000
print(numeros_telefones)

#IMPRESSAO ORDENADA DE UM DICIONARIO RETORNANDO VALORES 
for valores in numeros_telefones.keys():
    print(valores)

#ADICIONAR NOVOS ELEMENTOS A UM DICIONARIO USANDO O METODO UPDATE
numeros_telefones.update({"Aires": 874536789})
print(numeros_telefones)

#REMOVENDO ELEMENTOS DE UM DICIONARIO 
del numeros_telefones["Lina"]

#USANDO O METDOS POPINTEM PARA ELIMINAR O ULTIMO ELEMENTO
numeros_telefones.popitem()

#REMOVER TODOS INTENS DE UM DICIONARIO
numeros_telefones.clear()

#PARA CRIUARMOS UMA COPIA DE UM DICIONARIO 
novoNumerros= numeros_telefones.copy()





