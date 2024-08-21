from Carro import *
from Moto import *

# Criando objetos das subclasses
carro = Carro("Toyota", "Corolla", 2022, 4)
moto = Moto("Honda", "CB 500", 2021, "Esportivo")


# Usando métodos herdados e específicos das subclasses
print(carro)
carro.ligar()
carro.abrir_porta()
carro.desligar()

print("\n" + str(moto))
moto.ligar()
moto.empinar()
moto.desligar()
