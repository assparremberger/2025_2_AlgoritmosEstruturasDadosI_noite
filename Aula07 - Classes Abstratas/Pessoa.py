from Cidade import Cidade
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cid = Cidade("Itati") ):
        self.nome = nome
        self.cidade = cid

    @abstractmethod
    def imprimir(self):
        pass

    def __str__(self):
        txt = "Nome: " + self.nome
        #txt += "\nCidade: " + self.cidade.nome 
        txt += "\n" + str(self.cidade)
        return txt
        
        