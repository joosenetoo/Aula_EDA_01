from Livro import Livro  # Importando a classe Livro do arquivo Livro.py

class LivroFiccao(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas

    def calcular_preco(self):
        return self.paginas * 0.05  # Preço baseado no número de páginas
