class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def imprimir_informacoes(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

# Método __str__
    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.ano})"
