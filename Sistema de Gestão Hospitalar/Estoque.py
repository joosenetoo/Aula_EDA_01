class Estoque:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def listar_medicamentos(self):
        return [str(medicamento) for medicamento in self.medicamentos]
