numero=int(input("Digite o primeiro numero: "))

numerosPares=0
numerosImpares=0

while numero!=0:
    if numero%2==1:
        numerosPares=+1
    else: 
        numerosImpares=+1
    numero=int(input("Digite o proximo numero: "))

print("Os numeros pares sao: ", numerosPares)
print("Os numeros impares sao: ", numerosImpares)

    
    