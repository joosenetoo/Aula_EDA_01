class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

    def saudacao(self):
        return f"Olá, {self.nome}!"