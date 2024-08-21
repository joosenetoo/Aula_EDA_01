from abc import ABC, abstractmethod

class Livro(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def calcular_preco(self):
        pass
