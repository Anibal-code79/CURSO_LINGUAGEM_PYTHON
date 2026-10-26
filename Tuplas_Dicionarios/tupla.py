numeros_telefones= 1, 3, 5, 6, 7, 9
#IMPRESSAO DE TODOS DADOS DA TUPPLA
for numeros in numeros_telefones:
    print(numeros)

#IMPRESSAO DE UM DOS ELEMENTOS DE UMA TUPLA
print(numeros_telefones[0])

#VERIFICAR SE UMA CHAVE FAZ PARTE DE UMA TUPLA
if 7 in numeros_telefones:
    print("Sim ele faz parte da lista")
if 10 not in numeros_telefones:
    print("Nao faz parte da lista")

#VERIFICAR O NUMERO DE CHAVES E VALORES QUE FAZEM PARTE DE UMA LISTA DE TUPLA
print(len(numeros_telefones))

#CONTAR UM DICIONARIOE E ENCONTRRAR VALORES DUPLICADOS EM UMA TUPLA
duplicado= numeros_telefones.count(2)
print(duplicado)

