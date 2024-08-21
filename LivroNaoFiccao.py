from Livro import Livro  # Importando a classe Livro do arquivo livro.py

class LivroNaoFiccao(Livro):
    def __init__(self, titulo, autor, palavras):
        super().__init__(titulo, autor)
        self.palavras = palavras

    def calcular_preco(self):
        return self.palavras * 0.001  # Preço baseado no número de palavras