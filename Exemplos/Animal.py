class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome)  # Chama o __init__ da classe base Animal
        self.idade = idade

# Criando uma instância de Cachorro
meu_cachorro = Cachorro("Rex", 5)

print(meu_cachorro.nome)  # Saída: Rex
print(meu_cachorro.idade)  # Saída: 5

# Aqui, super().__init__(nome) chama o
# metodo __init__ da classe Animal para
# definir o atributo nome, e depois o
# atributo idade é definido em Cachorro.