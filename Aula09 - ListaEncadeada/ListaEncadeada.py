from No import No
# Lista Encadeada em ordem crescente
class ListaEncadeada:
     
    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado :
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None :
                    if nodo.dado < aux.dado:
                        ant.prox = nodo
                        nodo.prox = aux
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux is None:
                    ant.prox = nodo
        self.imprimir()

    def imprimir(self):
        print( "-----------------------------------")
        print( "Lista Encadeada em ordem crescente")
        if self.inicio is None:
            print(" -- Lista Vazia -- ")
        else:
            aux = self.inicio
            while aux != None:
                print( aux.dado )
                aux = aux.prox
        print( "-----------------------------------")
            

    def remove(self, valor):
        if self.inicio is None:
            print( "Nada removido, pois a lista está vazia")
        else:
            removeu = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu: 
                print( "Elemento " + valor + " removido!")
            else:
                print( "Elemento " + valor + " não encontrado!")
            
            self.imprimir()


    