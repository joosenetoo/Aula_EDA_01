class Aluno:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    # Getter
    def get_nome(self):
        return self.__nome

    # Setter
    def set_nome(self, nome):
        if nome:  # Validação simples
            self.__nome = nome

    def __str__(self):
        return self.__nome


class Curso:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado
        self.__alunos = []  # Atributo privado

    # Getter
    def get_nome(self):
        return self.__nome

    # Setter
    def set_nome(self, nome):
        if nome:  # Validação simples
            self.__nome = nome

    def matricular(self, aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.__alunos:
            print(aluno)


# Exemplo de uso
curso = Curso("Estrutura de Dados")
aluno1 = Aluno("Carlos")
aluno2 = Aluno("Ana")

curso.matricular(aluno1)
curso.matricular(aluno2)

curso.listar_alunos()
