class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)


# Exemplo de uso
func1 = Funcionario("Marcos")
func2 = Funcionario("Julia")

departamento = Departamento("TI")
departamento.adicionar_funcionario(func1)
departamento.adicionar_funcionario(func2)

departamento.listar_funcionarios()
