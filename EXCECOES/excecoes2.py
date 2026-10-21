try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Você não pode dividir por zero!")
except ValueError:
    print("Erro: Digite apenas números inteiros válidos.")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Operação finalizada.")
