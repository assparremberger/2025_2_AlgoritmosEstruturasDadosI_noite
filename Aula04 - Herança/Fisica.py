from Pessoa import Pessoa
from Cidade import Cidade

class Fisica( Pessoa ):
    def __init__(self, nome, cid = Cidade("POA"), cpf = None):
        super().__init__(nome, cid)
        self.cpf = cpf