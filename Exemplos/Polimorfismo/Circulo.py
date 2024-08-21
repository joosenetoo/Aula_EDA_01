import math
from Forma import *

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def __str__(self):
        return f"Circulo com raio {self.raio}"
