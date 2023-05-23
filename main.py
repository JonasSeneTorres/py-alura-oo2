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

class Playlist:
    def __init__(self, nome, programas):
        self.nome  = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()

atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()

grade_programas = [vingadores, atlanta]

minhaPlaylist = Playlist('minha playlist', grade_programas)

print(f"\nTamanho atual da da playlist: {len(minhaPlaylist)}\n")

for programa in minhaPlaylist:
    print(programa)



