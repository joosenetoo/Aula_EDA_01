class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"O {self.modelo} está ligado.")

    def desligar(self):
        print(f"O {self.modelo} está desligado.")

    def __str__(self):
        return f"{self.ano} {self.marca} {self.modelo}"
