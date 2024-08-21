from Forma import *

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def __str__(self):
        return f"Retangulo com largura {self.largura} e altura {self.altura}"
