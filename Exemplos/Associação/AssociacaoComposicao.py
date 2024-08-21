class Comodo:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []

    def adicionar_comodo(self, nome_comodo):
        comodo = Comodo(nome_comodo)
        self.comodos.append(comodo)

    def listar_comodos(self):
        for comodo in self.comodos:
            print(comodo)


# Exemplo de uso
casa = Casa("Rua das Flores, 123")
casa.adicionar_comodo("Sala")
casa.adicionar_comodo("Cozinha")
casa.adicionar_comodo("Quarto")

casa.listar_comodos()
