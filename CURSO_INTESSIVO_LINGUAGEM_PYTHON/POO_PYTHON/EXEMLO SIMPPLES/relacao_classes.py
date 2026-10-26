class Curso:
    def __init__(self, nome, ano):
        self.nome= nome
        self.ano= ano

class Estudante:
    def __init__(self, nome, curso):
        self.nome= nome
        self.curso= curso

curso= Curso("Informatica", 2026)
estudante= ("Anibal", curso)

print("O estudante", estudante.nome, "esta a fazer o curso de ", estudante.curso.nome,"do ano de ", estudante.curso.ano)