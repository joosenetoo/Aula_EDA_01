class Consulta:
    def __init__(self, paciente, funcionario, data):
        self.paciente = paciente
        self.funcionario = funcionario
        self.data = data

    def __str__(self):
        return (f"Consulta: Paciente - {self.paciente.nome}, Médico - {self.funcionario.nome}, "
                f"Data: {self.data}")
