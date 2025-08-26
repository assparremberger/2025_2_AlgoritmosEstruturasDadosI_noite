from Cidade import Cidade
class Pessoa:
    def __init__(self, nome, cid = Cidade("Itati") ):
        self.nome = nome
        self.cidade = cid
        