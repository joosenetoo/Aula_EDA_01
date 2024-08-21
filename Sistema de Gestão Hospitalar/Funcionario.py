class Funcionario:
    def __init__(self, nome, cargo, turno):
        self.nome = nome
        self.cargo = cargo
        self.turno = turno

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Turno: {self.turno}"
