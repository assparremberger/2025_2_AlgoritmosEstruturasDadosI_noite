from Pessoa import Pessoa
from Cidade import Cidade

class Fisica( Pessoa ):
    def __init__(self, nome, cid = Cidade("POA"), cpf = None):
        super().__init__(nome, cid)
        self.cpf = cpf
        self.__altura = 0

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, valor):
        if valor >0:
            self.__altura = valor
            

    def __str__(self):
        return super().__str__() + "\nCPF: " + self.cpf