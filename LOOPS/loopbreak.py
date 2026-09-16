#VERIFICACAO DE  NUMERO MAIOR NOS NUMEROS DIGITADOS PELO USUARIO
numero_maior = None

while True: 
    numero = int(input("Digite um numero: "))
    if numero == 10:
        break
        
    if numero_maior is None or numero > numero_maior:
        numero_maior = numero

if numero_maior is not None:
    print("O numero maior de todos os numeros que digitou e: ", numero_maior)
else:
    print("Nenhum numero válido foi digitado antes do 10.")
