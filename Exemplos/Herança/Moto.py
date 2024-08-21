from Veiculo import *

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_guidao):
        super().__init__(marca, modelo, ano)
        self.tipo_guidao = tipo_guidao

    def empinar(self):
        print(f"A moto {self.modelo} está empinando!")

    def __str__(self):
        return f"{super().__str__()} - Guidão: {self.tipo_guidao}"
