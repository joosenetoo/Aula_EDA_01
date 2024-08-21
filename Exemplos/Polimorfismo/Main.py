from Circulo import *
from Retangulo import *

def imprimir_area(forma):
    print(f"A área da forma ({forma}) é {forma.area()}")

# Criando objetos das subclasses
circulo = Circulo(5)
retangulo = Retangulo(4, 6)

# Testando o polimorfismo
imprimir_area(circulo)
imprimir_area(retangulo)
