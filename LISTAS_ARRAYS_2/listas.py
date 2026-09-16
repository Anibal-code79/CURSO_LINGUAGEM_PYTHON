#CRIACAO DE NOVAS LISTAS 
lista=[10,6,18,19,10,17]
maior=lista[0]

def verificar(valor):
    if valor in lista:
        return "O numero esta na lista"
    if valor not in lista:
        return "O numero nao esta na lista"

#VERIFICCAR MAIOR NUMERO NA LISTA
for i in range(len(lista)):
    if lista[i]>maior:
        maior=lista[i]
print("O maior valor da lista: ", maior)

novaLista=lista[1:4:2]
print(novaLista)

#ELIMINAR PARTES DE UMA LISTAS 
del lista[2:4]
print(lista)

#VERFICANDO SE EXISTE UM DETERMINADO VALOR NUMA LISTA
valor=int(input("Digite o numero que deseja saber se esta ou nao na lista: "))
print(verificar(valor))