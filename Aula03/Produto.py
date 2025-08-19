from Categoria import Categoria

class Produto:

    def __init__(self, nome, preco = 10, cat = Categoria("Alimentos") ):
        self.nome = nome
        self.preco = preco
        self.categoria = cat

    def __str__(self):
        txt = "Produto: " + self.nome
        txt += "\nPreço: " + str( self.preco)
        #txt += "\nCategoria: " + self.categoria.nome
        txt += "\n" + str( self.categoria )
        return txt