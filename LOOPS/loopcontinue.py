#PEDIR NUMEROS AO ULTILOZADOR E SOMA LOS filtrando numeros negativos 
soma=0
contador=0
while contador<3:
    numero=int(input("Digite um numero posetivo: "))

    if numero<0:
        continue
    soma+=numero
    contador+=1

print("A soma dos numeros digitados e: ",soma)