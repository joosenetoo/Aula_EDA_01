class Paciente:
    def __init__(self, nome, idade, prontuario):
        self.nome = nome
        self.idade = idade
        self.prontuario = prontuario

    def __str__(self):
        return f"Paciente: {self.nome}, Idade: {self.idade}, Prontuário: {self.prontuario}"
