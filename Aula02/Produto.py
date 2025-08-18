#Construir a classe Produto, que possui o atributo nome.
#Criar uma instância de Produto e printar esta instância
class Produto:
    def __init__(self, name = None):
        self.nome = name


p = Produto( "Coca-Cola" )
p2 = Produto( "Pepsi" )

print( p , " - ",  p.nome)
print( p2 , " - ",  p2.nome)



# p2 = Produto( "Pepsi" )
# print( p.nome )