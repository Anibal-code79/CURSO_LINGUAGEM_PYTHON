def situacao(media):
    if media>10:
        return "Aprovado"
    else: 
        return "Reprovado"

nome=input("Digite o nome do Aluno: ")
notas=[]

for i in range(3):
    nota=float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

soma=0
for i in range(len(notas)):
    soma+=notas[i]

media= soma/len(notas)

print("O nome do estudante: ", nome)
print("Media do estudante: ", media)
print("Situacao do estudante: ", situacao(media))
