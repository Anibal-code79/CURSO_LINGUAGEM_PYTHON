def verificarMaiorNota(notas):
    maior=max(notas)
    return maior

def verificarSituacao(media):
    if media>=10:
        return "Aluno Aprovado"
    else:
        return "Aluno Reprovado"
def somarNotas(notas):
    s=0
    for i in range(len(notas)):
        s+=notas[i]
    return s

nome=input("Digite o nome do estudante: ")
notas=[]
for i in range(3):
    nota=float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

print("Nome do estudante: ",nome)
maiorNota=verificarMaiorNota(notas)
print("A maior nota: ", maiorNota)

soma=somarNotas(notas)
media=soma/len(notas)
print("A media do estudante: ", media)
resultado= verificarSituacao(media)
print("Situacao do estudante: ", resultado)
