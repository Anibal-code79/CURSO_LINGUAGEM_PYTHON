print("=======CADASTRO NA AULA PYTHON======")
print("Digite seu nome: ")
nome=input()
print("Digite sua Idade")
idade=input()
print("Digite sua senha: ")
senha=input()
print("Confirme sua senha: ")
confirmar_senha=input()
if senha==confirmar_senha :
    print("Ola ",nome,"com a sua idade de ",idade," anos!! Seja bem Vindo a nossa aula de python")
else :
    print("Senha incorrecta")