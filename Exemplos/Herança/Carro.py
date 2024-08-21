from Veiculo import *

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da superclasse
        self.numero_portas = numero_portas

    def abrir_porta(self):
        print(f"Portas do {self.modelo} estão abertas.")

    def __str__(self):
        return f"{super().__str__()} - {self.numero_portas} portas"
