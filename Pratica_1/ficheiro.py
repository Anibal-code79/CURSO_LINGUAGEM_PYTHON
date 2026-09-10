def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def verificar_situacao(media):
    if media >= 10:
        return "Aprovado"
    else:
        return "Reprovado"

print("===SISTEMA SIMPLES DE NOTAS===")

nome = input("Nome do estudante: ")
idade = int(input("Idade: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
resultado = verificar_situacao(media)

print("\n========== RESULTADO ==========")
print("Nome:", nome)
print("Idade:", idade)
print("Media: ", media)
print("Situação:", resultado)
print("===============================")