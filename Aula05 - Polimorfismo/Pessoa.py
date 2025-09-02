from Cidade import Cidade
class Pessoa:
    def __init__(self, nome, cid = Cidade("Itati") ):
        self.nome = nome
        self.cidade = cid

    def __str__(self):
        txt = "Nome: " + self.nome
        #txt += "\nCidade: " + self.cidade.nome 
        txt += "\n" + str(self.cidade)
        return txt
        