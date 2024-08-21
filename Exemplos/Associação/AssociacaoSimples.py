class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)


# Exemplo de uso
curso = Curso("Estrutura de Dados")
aluno1 = Aluno("Carlos")
aluno2 = Aluno("Ana")

curso.matricular(aluno1)
curso.matricular(aluno2)

curso.listar_alunos()
