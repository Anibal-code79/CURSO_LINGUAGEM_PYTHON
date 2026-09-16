import time

numero=int(input("Digite um numero e veja a sua tabuada em dois a cada dois segundos: "))
for i in range(2,10,2):
    print(numero," x ",i," = ", numero*i)
    time.sleep(2)
print("Prontos ja esta! ")
