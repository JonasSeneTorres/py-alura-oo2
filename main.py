class ProgramaTV:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(ProgramaTV):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"

class Serie(ProgramaTV):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome}  - {self.ano} - {self.temporadas} temporadas - {self.likes} likes"


vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()

atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()

grade_programas = [vingadores, atlanta]

for programa in grade_programas:
    print(programa)

lista = [1, 2, 4, 5]

