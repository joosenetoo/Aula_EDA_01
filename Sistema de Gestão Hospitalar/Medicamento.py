class Medicamento:
    def __init__(self, nome, lote, validade):
        self.nome = nome
        self.lote = lote
        self.validade = validade

    def __str__(self):
        return (f"Medicamento: {self.nome}, Lote: {self.lote}, Validade: {self.validade}")
